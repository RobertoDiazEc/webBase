"""The dashboard page."""

from ..templates import template
from .. import styles
from ..utilis import lang
from ..views.empresa.serredx import serheaderedx, sersomosredx, serserviciosredx
import reflex as rx
import reflex_chakra as rc

@template(route="/", title="REDx Soluciones",routeimagen="/imagenes/portadaRedx1.jpg")
def redx_inicio() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.box(
            lang(),
            rx.vstack(
                serheaderedx("/imagenes/bienvenidos2.jpg"),
                rx.divider(),
                sersomosredx("/imagenes/programacion.png"),
                rx.divider(),
                rx.flex(
                rx.hstack(
                    serserviciosredx(
                        "Desarrollo",
                        "nos acoplamos a tu presupuesto",
                        "/imagenes/programacion2.png",

                    ),
                    serserviciosredx(
                        "Servicio Tecnico",
                        "nos acoplamos a tu presupuesto",
                        "/imagenes/programacion3.png",

                    ),
                    serserviciosredx(
                        "Venta de Equipos",
                        "nos acoplamos a tu presupuesto",
                        "/imagenes/programacion4.png",

                    ),
                ),
                spacing="2",
                align_items="flex-start",
                flex_wrap="wrap"
                ),    
                spacing="4",
                width="100%",
            ),
        
    width="100%",
)