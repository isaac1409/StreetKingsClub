import reflex as rx
from StreetKingsClub.frontend.pages import home, loginPage
from .frontend.pages.usuarios import index, detalles, editar, crear, eliminar
from StreetKingsClub.backend.auth import AuthState

app = rx.App(
    theme=rx.theme(
        appearance="light", 
        has_background=True
    ),
    on_load=rx.remove_local_storage("chakra-ui-color-mode")
)
#LOGIN
app.add_page(loginPage, route="/login")

#HOMEPAGE
app.add_page(home, route="/", on_load=AuthState.check_login)

#USUARIOS
app.add_page(index, route="/usuarios/", on_load=AuthState.check_login)
