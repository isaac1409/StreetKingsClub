import reflex as rx
from reflex import route
from ...backend.usuarios import get_usuario, get_usuarios, crear_usuario, editar_usuario, delete_usuario
from ...backend.auth import AuthState

def index():
    return rx.flex(
        rx.script(src="https://cdn.jsdelivr.net/npm/sweetalert2@11"),
        rx.button("Cerrar Sesión", on_click=AuthState.logout),
        width="100vw",
        height="100vh",
    )

def detalles():
    return rx.flex()

def crear():
    return rx.flex()

def editar():
    return rx.flex()

def eliminar():
    return rx.flex()