import reflex as rx
from reflex.style import set_color_mode, color_mode

def dark_mode_toggle() -> rx.Component:
    return rx.segmented_control.root(
        rx.segmented_control.item(
            rx.icon(tag="monitor", size=20),
            value="system",
        ),
        rx.segmented_control.item(
            rx.icon(tag="sun", size=20),
            value="light",
        ),
        rx.segmented_control.item(
            rx.icon(tag="moon", size=20),
            value="dark",
        ),
        on_change=set_color_mode,  # Actualiza el color cuando el toggle cambie
        variant="classic",  # Estilo del toggle
        radius="large",  # Bordes redondeados
        value=color_mode,  # Estado actual del color (claro, oscuro, o sistema)
    )
