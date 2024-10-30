import reflex as rx
from ...backend.usuarios import get_usuario, get_usuarios, crear_usuario, editar_usuario, delete_usuario
from ...backend.auth import AuthState
from ...frontend.templates.formularios import template

def indexUsuarios():
    return template(
        #rx.color_mode.button(position="top-right"),
        rx.heading("Usuarios", size="9",),
        rx.script(src="https://cdn.jsdelivr.net/npm/sweetalert2@11"),
        rx.data_table(
            data=get_usuarios(),
            pagination=False,
            search=True, 
            sort=True,
        ),
    )

def detallesUsuario():
    return template(
        rx.color_mode.button(position="top-right"),
    )

def crearUsuario():
    return template(
        rx.color_mode.button(position="top-right"),
    )

def editarUsuario():
    return template(
        rx.color_mode.button(position="top-right"),
    )

def eliminarUsuario():
    return template(
        rx.color_mode.button(position="top-right"),
    )