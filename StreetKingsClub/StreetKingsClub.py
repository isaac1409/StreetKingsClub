import reflex as rx
from StreetKingsClub.frontend.pages import home, loginPage, homePage
from StreetKingsClub.backend.auth import AuthState

app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True
    ),
    on_load=rx.remove_local_storage("chakra-ui-color-mode")
)

app.add_page(loginPage, route="/login", on_load=AuthState.check_already_logged_in)  # Verifica si ya está autenticado
app.add_page(homePage, route="/homepage", on_load=AuthState.check_login)  # Verifica autenticación
app.add_page(home, route="/", on_load=AuthState.check_login)  # Verifica autenticación
