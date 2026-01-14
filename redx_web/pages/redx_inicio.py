
import reflex as rx
from redx_web.templates import template
from redx_web.styles import BASE_STYLE, STYLESHEETS

from redx_web.views.empresa.serredx import serheaderedx, sersomosredx
from redx_web.views.secciones.seccionredx import serviciosredx, productosredx, automatizacionredx
from redx_web.views.charts import chart
from redx_web.utilis import default_meta
from redx_web.ui.routes import Route, RouteImagen
from redx_web.components.promo_redx import inicio_section, inicio_section2


all_meta = [*default_meta, *[]]


    
   
    

@rx.page(route=Route.INDEX.value, title="REDx Soluciones", meta=all_meta)
@template(routeimagen=RouteImagen.PORTADA.value)
def redx_inicio() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.box(
            inicio_section(),
            rx.divider(),
            inicio_section2(),
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