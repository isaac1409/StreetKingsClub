from sqlmodel import select
from ..database import get_session
from ..modelos import Usuario
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def get_usuarios():
    try:
        with get_session() as session:  
            usuarios = session.exec(select(Usuario)).all()
            return usuarios
    except Exception as e:
        session.rollback()
        raise Exception(f"Error al obtener los usuarios")

def get_usuario(id: int):
    try:
        with get_session() as session:  
            usuario = session.get(Usuario, id)
            if usuario is None:
                raise ValueError(f"Usuario no encontrado")
            return usuario
    except Exception as e:
        session.rollback()
        raise Exception(f"Error al obtener el usuario")

def crear_usuario(usuario: Usuario):
    try:
        with get_session() as session:  
            existing_user = session.exec(select(Usuario).where(Usuario.Username == usuario.Username)).first()
            if existing_user:
                raise ValueError(f"El nombre de usuario '{usuario.Username}' ya está en uso.")
            usuario.Password = get_password_hash(usuario.Password)
            session.add(usuario)
            session.commit()
            session.refresh(usuario)
            return usuario
    except Exception as e:
        session.rollback()
        raise Exception(f"Error al crear el usuario")

def editar_usuario(id: int, usuario: Usuario):
    try:
        with get_session() as session:  
            db_usuario = session.get(Usuario, id)
            if not db_usuario:
                raise ValueError(f"Usuario no encontrado")
            db_usuario.Username = usuario.Username
            db_usuario.Password = get_password_hash(usuario.Password)
            session.add(db_usuario)
            session.commit()
            session.refresh(db_usuario)
            return db_usuario
    except Exception as e:
        session.rollback()
        raise Exception(f"Error al editar el usuario")

def delete_usuario(id: int):
    try:
        with get_session() as session:  
            usuario = session.get(Usuario, id)
            if usuario is None:
                raise ValueError(f"Usuario no encontrado")
            session.delete(usuario)
            session.commit()
            return {"detail": "Usuario eliminado correctamente"}
    except Exception as e:
        session.rollback()
        raise Exception(f"Error al eliminar el usuario")