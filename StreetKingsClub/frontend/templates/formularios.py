import reflex as rx
from ...frontend.components.sidebar import sidebar_bottom_profile as sidebar

def templateDesktop(*children):
    return rx.flex(
        rx.script(src="https://cdn.jsdelivr.net/npm/sweetalert2@11"),
        sidebar(),
        rx.box(
        rx.vstack(
            *children,
            width="90%",
            margin="20px 40px",
        ),
            width="100%",
            height="100%",
        ),
        width="100vw",
        height="100vh",
    )

def templateMobile(*children):
    return rx.flex(
        rx.script(src="https://cdn.jsdelivr.net/npm/sweetalert2@11"),
        sidebar(),
        rx.box(
        rx.vstack(
            *children,
            width="100%",
            padding="0px 10px",
        ),
            width="100%",
            height="100%",
        ),
        width="100vw",
        height="100vh",
    )

def template(*children):
    return rx.flex(
        rx.script(src="https://cdn.jsdelivr.net/npm/sweetalert2@11"),
        sidebar(),
        rx.box(
            rx.vstack(
                *children,
                width=rx.breakpoints(initial="100%", md="90%"),
                padding=rx.breakpoints(initial="10px 10px", md="20px 40px"),
                margin=rx.breakpoints(initial="0", md="20px 40px"),
            ),
            width="100%",
            height="100%",
        ),
        width="100vw",
        height="100vh",
    )