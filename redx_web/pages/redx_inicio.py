

from ..templates import template
from .. import styles

from ..views.empresa.serredx import serheaderedx, sersomosredx
from ..views.secciones.seccionredx import serviciosredx, productosredx
from ..utilis import default_meta
import reflex as rx

all_meta = [*default_meta, *[]]


    
   
    

@rx.page(route="/", title="REDx Soluciones", meta=all_meta)
@template(routeimagen="/imagenes/portadaRedx1.jpg")
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