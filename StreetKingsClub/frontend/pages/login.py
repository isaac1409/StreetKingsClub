import reflex as rx
from StreetKingsClub.backend.auth import AuthState

def loginPage():
    return rx.flex(
        rx.box(
            rx.center(rx.heading("Bienvenido a tu liga", size="8", margin_bottom="10px", color="black")),
            rx.center(rx.heading("Ingrese sus credenciales para continuar", size="3", margin_bottom="20px", color="black")),
            rx.separator(
                margin_bottom="20px",
            ),
            rx.center(
            rx.vstack(
                rx.input(
                    placeholder="Usuario",
                    on_change=lambda value : AuthState.set_username(value),
                    size="3",
                    width="300px",
                    background_color="#ddd",
                    color="black",
                    style={"& input::placeholder": {"color": "#777"}},
                ),
                rx.input(
                    type="password",
                    placeholder="Contraseña",
                    on_change=lambda value: AuthState.set_pass(value),
                    on_key_down=AuthState.handle_key_down,
                    size="3",
                    width="300px",
                    background_color="#ddd",
                    color="black",
                    style={"& input::placeholder": {"color": "#777"}},
                    margin_bottom="10px",
                ),
                rx.script(src="https://cdn.jsdelivr.net/npm/sweetalert2@11"),
                rx.button("Iniciar Sesión", on_click=AuthState.login, size="3", width="10em", style={"background_color": "#3085d6"},),
                spacing="4",
                align_items="center",
            )),
            background="#ffffff",
            border="1px solid #eaeaea",
            padding="16px",
            width="400px",
            height="320px",
            border_radius="8px",
        ),
        width="100vw",
        height="100vh",
        justify="center",
        align="center",
        style={
            "backgroundImage": "url('https://wallpapers.com/images/high/cool-soccer-nature-field-xx9ly9v0yostbag2.webp')",
            "backgroundSize": "cover",         
            "backgroundPosition": "center",     
            "backgroundRepeat": "no-repeat",    
            "height": "100vh",                 
        },
        on_mount=AuthState.check_login
    )