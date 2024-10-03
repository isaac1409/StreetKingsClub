import reflex as rx

def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )

def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Dashboard", "layout-dashboard", "/dashboard"),
        sidebar_item("Equipos", "square-library", "/teams"),
        sidebar_item("Estadisticas", "bar-chart-4", "/stats"),
        sidebar_item("Mensajes", "mail", "/messages"),
        spacing="1",
        width="100%", 
    )

def sidebar() -> rx.Component:
    return rx.box( 
        rx.vstack(
            rx.hstack(
                rx.image(src="/logo.jpg", width="2.25em", border_radius="25%"), 
                rx.heading("StreetKingsClub", size="5", weight="bold"),
                align="center",
                justify="start",
                padding_x="0.5rem",
            ),
            sidebar_items(),
            rx.spacer(),
            sidebar_item("Settings", "settings", "/settings"),
            sidebar_item("Log out", "log-out", "/logout"),
            spacing="1",
            padding="1.5em",
            bg=rx.color("accent", 3),
            height="100vh",  # Ocupa el 100% de la altura de la pantalla
            width="16em",
        ),
    )
