import reflex as rx
from rxconfig import config
from StreetKingsClub.frontend.components.sidebar import sidebar  # Importar sidebar

def homePage() -> rx.Component:
    return rx.box(
        rx.hstack(
            sidebar(),  # Agregar el sidebar aquí
            rx.container(
                rx.vstack(
                    rx.heading("Welcome to StreetKingsClub!", size="9"),
                    rx.text(
                        "Este es el contenido de la home page",
                        size="5",
                    ),
                    rx.link(
                        rx.button("Check out our docs!"),
                        href="https://reflex.dev/docs/getting-started/introduction/",
                        is_external=True,
                    ),
                    spacing="5",
                    justify="center",
                    align="center",  # Alinear el contenido en el centro
                    width="100%",  # Asegurar que ocupe todo el ancho restante
                    min_height="85vh",
                ),
                max_width="100%",  # Permite que el contenido crezca para llenar el espacio
                padding="2em",  # Agregar un poco de padding para que no quede pegado al sidebar
            ),
        ),
        bg="black",  # Asegura que el fondo sea oscuro como en la captura
        min_height="100vh",  # Ocupa toda la altura de la pantalla
    )
