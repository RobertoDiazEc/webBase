"""The dashboard page."""

from ..templates import template

import reflex as rx
import reflex_chakra as rc

@template(route="/", title="redx_inicio")
def redx_inicio() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
       # rx.heading("CI Job Dashboard", size="5"),
       # main_table(),
        rc.heading("REDx Soluciones"),
        rc.center("Ingeniria de Sistemas"),
        rc.button(
               "click me",
               on_click=rx.toast("show toast!"),
               bg="purple",
               border_radius="0.5em",
               pl="10px"
           ),
   
        spacing="8",
        width="100%",
    )
