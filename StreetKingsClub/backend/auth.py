import reflex as rx
from ..modelos import Usuario
from ..database import get_session
from sqlmodel import select
import jwt
import secrets
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class AuthState(rx.State):
    usuario : str = ""
    password : str = ""
    token: str = rx.LocalStorage()
    ultima: str = rx.LocalStorage()
    anterior: str = rx.LocalStorage()

    def logout(self):
        self.usuario = ""
        self.password = ""
        self.token = ""
        self.ultima = ""
        self.reset()
        return rx.redirect("/login")

    def check_login(self):
        if not self.logged_in:
            if self.token != "" and self.router.page.path != "/login":
                self.anterior = self.usuario
                self.usuario = ""
                self.password = ""
                self.token = ""
                yield AuthState.mostrarAlerta("Oooops!", " Parece que permaneciste demasiado tiempo inactivo, vuelve a iniciar sesión", "warning")
            return rx.redirect("/login")
        else:
            self.renew_token_if_needed()
            if self.router.page.path != "/login":
                self.ultima = self.router.page.path
            else:
                return rx.redirect(self.ultima)
        
    @rx.var
    def logged_in(self) -> bool:
        return self.token != "" and self.verify_token(self.token)
    
    def set_username(self, value: str):
        self.usuario = value

    def set_pass(self, value: str):
        self.password = value
    
    def verify_password(self, password: str, hashed_password: str):
        return pwd_context.verify(password, hashed_password)

    def login(self):
        with get_session() as session:
            user = session.exec(
                select(Usuario).where(Usuario.Username == self.usuario)
            ).first()
            if user and self.verify_password(self.password, user.Password):
                self.token = self.create_jwt_token(user.Username)
                if self.ultima != "" and self.anterior == self.usuario:
                    return rx.redirect(self.ultima)
                else:
                    yield AuthState.mostrarAlerta(f"{user.Nombre}, bienvenid@ a tu portal", "", "success")
                    return rx.redirect("/")
            else:
                return AuthState.mostrarAlerta("Error", "Verifica tus credenciales", "error")
    
    def mostrarAlerta(self, titulo, texto, tipo):
        return rx.call_script(
                    "Swal.fire({"
                        f"title: '{titulo}',"
                        f"text: '{texto}',"
                        f"icon: '{tipo}',"
                        "confirmButtonText: 'OK',"
                        "confirmButtonColor: '#3085d6',"
                    "})"
                )
    
    def create_jwt_token(self, username: str):
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = {"sub": username, "exp": expire}
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def verify_token(self, token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                return False
            return True
        except jwt.ExpiredSignatureError:
            return False
        except jwt.PyJWTError:
            return False 

    def renew_token_if_needed(self):
        try:
            payload = jwt.decode(self.token, SECRET_KEY, algorithms=[ALGORITHM])
            exp = datetime.fromtimestamp(payload.get("exp"), tz=timezone.utc)
            remaining_time = exp - datetime.now(tz=timezone.utc)
            if remaining_time.total_seconds() < 300:
                self.token = self.create_jwt_token(payload.get("sub"))
        except jwt.ExpiredSignatureError:
            self.logout()
        except jwt.PyJWTError:
            return False
    
    def handle_key_down(self, key: str):
        if key == "Enter":
            return AuthState.login