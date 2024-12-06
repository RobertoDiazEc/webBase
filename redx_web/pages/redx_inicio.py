

from ..templates import template
from .. import styles

from ..views.empresa.serredx import serheaderedx, sersomosredx
from ..views.secciones.seccionredx import serviciosredx, productosredx
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
                serheaderedx("/imagenes/bienvenidos2.jpg"),
                rx.divider(),
                sersomosredx("/imagenes/programacion.png"),
                rx.divider(),
                serviciosredx(),
                rx.divider(),
                productosredx(),    
                spacing="4",
                width="100%",
            ),
        
    width="100%",
)