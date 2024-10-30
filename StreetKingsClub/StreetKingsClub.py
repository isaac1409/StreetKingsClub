import reflex as rx
from StreetKingsClub.frontend.pages import home, loginPage
from .frontend.pages.usuarios import indexUsuarios, detallesUsuario, editarUsuario, crearUsuario, eliminarUsuario
from StreetKingsClub.backend.auth import AuthState


app = rx.App()
#LOGIN
app.add_page(loginPage, route="/login")

#HOMEPAGE
app.add_page(home, route="/", on_load=AuthState.check_login)

#USUARIOS
app.add_page(indexUsuarios, route="/usuarios", on_load=AuthState.check_login)
"""
app.add_page(detallesUsuario, route="/usuarios/detalles/[username]", on_load=AuthState.check_login)
app.add_page(crearUsuario, route="/usuarios/crear", on_load=AuthState.check_login)
app.add_page(editarUsuario, route="/usuarios/editar/[username]", on_load=AuthState.check_login)
app.add_page(eliminarUsuario, route="/usuarios/eliminar/[id]", on_load=AuthState.check_login)
"""