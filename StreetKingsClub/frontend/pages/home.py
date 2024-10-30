import reflex as rx
from rxconfig import config
from ...backend.auth import AuthState
from ..templates.formularios import template

def home() -> rx.Component:
    return template(
        #rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            rx.button("Cerrar Sesión", on_click=AuthState.logout),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )