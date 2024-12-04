"""The dashboard page."""

from ..templates import template
from .. import styles
import reflex as rx
import reflex_chakra as rc

@template(route="/", title="REDx Soluciones",routeimagen="/imagenes/portadaRedx1.jpg")
def redx_inicio() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.box(
            rx.vstack(
                rx.fragment(
                    #rc.color_mode_button(rc.color_mode_icon(), float="right"),
                    rc.vstack(
                        rc.heading("Welcome to my homepage!", font_size="2em"),
                        rc.link("Protected Page", href="/protected"),
                        spacing="1.5em",
                        padding_top="10%",
                    ),
                ),
                rc.heading("Quienes somos"),
                rc.center("Ingeniria de Sistemas"),
                rc.button(
                    "click me",
                    on_click=rx.toast("show toast!"),
                    bg="purple",
                    border_radius="0.5em",
                    pl="10px"
                ),
                spacing="4",
                width="100%",
            ),
        
    width="100%",
)