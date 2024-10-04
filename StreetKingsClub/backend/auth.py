import reflex as rx
from ..modelos import Usuario
from ..database import get_session
from sqlmodel import select

class AuthState(rx.State):
    usuario : str = ""
    password : str = ""

    def logout(self):
        self.usuario = None
        self.reset()
        return rx.redirect("/")

    def check_login(self):
        if not self.logged_in:
            return rx.redirect("/login")
        else:
            return rx.redirect("/")
        
    @rx.var
    def logged_in(self) -> bool:
        return self.usuario != "" and self.password != ""
    
    def set_username(self, value: str):
        self.usuario = value

    def set_pass(self, value: str):
        self.password = value

    def login(self):
        with get_session() as session:
            user = session.exec(
                select(Usuario).where(Usuario.Username == self.usuario)
            ).first()
            if user and user.Password == self.password:
                self.usuario = user.Username
                yield AuthState.mostrarAlerta("Sesión iniciada", f"Bienvenido a tu portal, {user.Nombre}","success")
                return rx.redirect("/") 
            else:
                return AuthState.mostrarAlerta("Error", "Verifica tus credenciales", "error")
            
    def get_users(self):
        with get_session() as session:
            users = session.exec(Usuario).all()
            return users
    
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
        
    
