"""The dashboard page."""

from ..templates import template
import redx_web.backend.page_state as pagestate
from ..views.usuariosapi import usuarioswebapi

import reflex as rx


@rx.page(route="/usuariosweb", title="Usuarios", on_load=pagestate.PageState.usuarios_dataweb)
@template(routeimagen="")
def usuariosweb() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.container(
        rx.vstack(
            rx.heading("usuarios registrados", 
                       size="5",
                       padding_top="15%"
                       ),
            usuarioswebapi(),
    
            spacing="4",
            width="100%",
        ),
        padding="15px 25px",
        width="100%",

    )