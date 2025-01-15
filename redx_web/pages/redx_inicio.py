

from ..templates import template
from .. import styles

from ..views.empresa.serredx import serheaderedx, sersomosredx
from ..views.secciones.seccionredx import serviciosredx, productosredx, automatizacionredx
from ..views.charts import chart
from ..utilis import default_meta
from ..ui.routes import Route, RouteImagen
import reflex as rx

all_meta = [*default_meta, *[]]


    
   
    

@rx.page(route=Route.INDEX.value, title="REDx Soluciones", meta=all_meta)
@template(routeimagen=RouteImagen.PORTADA.value)
def redx_inicio() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.box(
          
            rx.vstack(
                serheaderedx(RouteImagen.BIENVENIDO.value),
                rx.divider(),
                sersomosredx(RouteImagen.SOMOSREDX.value),
                rx.divider(),
                serviciosredx(),
                rx.divider(),
                automatizacionredx(),
                rx.divider(),
                chart(),
                rx.divider(),
                productosredx(),  
                spacing="4",
                width="100%",
            ),
        
    width="100%",
)