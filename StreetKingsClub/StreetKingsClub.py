import reflex as rx
from StreetKingsClub.frontend.pages import home, loginPage, homePage
from StreetKingsClub.backend.auth import AuthState

app = rx.App(
    theme=rx.theme(
        appearance="dark",
    )
)

app.add_page(loginPage, route="/login")
app.add_page(home, route="/", on_load=AuthState.check_login)
app.add_page(homePage, route="/homepage", on_load=AuthState.check_login)  # HomePage migrar a raiz
