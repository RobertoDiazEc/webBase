import reflex as rx

import reflex_chakra as rc

from ..stylesRD.stylespag import Size
from ..stylesRD.stylespag import title_body_style
from ..constants  import Constants
from ..components.title import title
from .index_imagen import imageninfo
from ..views.empresa.empresadet import Empresadetvalores
from ..views.empresa.empresadet import Empresadetobjetivos



def serheaderedx(imginfo: str) -> rx.Component:
    return rx.fragment(
                    #rc.color_mode_button(rc.color_mode_icon(), float="right"),
                    rx.hstack(
                    rc.vstack(
                        rc.heading("TE DAMOS LA BIENVENIDA!", font_size="2em"),
                        rc.center("REDx Soluciones es el aliado perfecto que estabas buscando en el desarrollo y soporte tecnológico. Brindamos Soluciones en tiempos reales, mejoramos procesos, reducimos costos."),
                        rc.center("Desarrollo de Software a Medida"), 
                        rc.center("Soporte Técnico 24/7"), 
                        rc.center("Consultoría en TI"),
                        rc.link("Registrate", href="/protected"),
                        spacing="1.5em",
                        padding="5%",
                    ),
                    imageninfo(imginfo),
                    #padding_top="10%", 
                    ),
                ),

def sersomosredx(imginfo: str) -> rx.Component:
    return rx.fragment(
                    #rc.color_mode_button(rc.color_mode_icon(), float="right"),
                    rx.hstack(
                        rc.vstack(
                            rc.heading("Quienes somos"),
                            rc.center("mi nombre es Roberto Diaz, soy Desarrollador de Sistemas por mas de 15 años en area de produccion, facturacion, bodega, contabilidad, integracion, implementacion de modelos personalizados."),
                            rc.center("Desarrollamos aplicaciones web, móviles y de escritorio utilizando tecnologías como Visual, C+, Python, Reflex, JavaScript, PHP, y más."),
                            rc.center("Ofrecemos soporte técnico 24/7 para resolver cualquier problema tecnológico rápidamente."),
                            rc.center("Ayudamos a tu empresa a optimizar su infraestructura tecnológica y fortalecer su ciberseguridad."),
                           spacing="1.0em",
                           padding="5%", 
                        ),
                        imageninfo(imginfo),
                        #padding_top="10%", 
                    ),
                ),


def serempresainfo(titulo: str, detalle: str, imginfo: str) -> rx.Component:
    return rx.box(
           title(titulo),
           rx.text(
                detalle,
                style=title_body_style),
            imageninfo(imginfo),
            rx.divider(),            
            padding=Size.MEDIUM.value,
            border=Size.ZERO,
            width="100%"
        )


def serempresaValores(titulop: str, imginfop: str) -> rx.Component:
    return rx.box(
        title(titulop),
        rx.list.unordered(
            rx.list.item(Empresadetvalores.CREATIVIDAD.value),
            rx.list.item(Empresadetvalores.CUMPLIMIENTO.value),
            rx.list.item(Empresadetvalores.INTEGRIDAD.value),
            style=title_body_style
            ),
        imageninfo(imginfop),
        rx.divider(),           
        ppadding= "10px",
        border=Size.ZERO,
        width="100%"    
)

def serempresaObjetivos(tituloo: str, imginfoo: str) -> rx.Component:
    return rx.box(
        title(tituloo),
        rx.list.unordered(
            rx.list.item(Empresadetobjetivos.OBJETIVO1.value),
            rx.list.item(Empresadetobjetivos.OBJETIVO2.value),
            rx.list.item(Empresadetobjetivos.OBJETIVO3.value),
            rx.list.item(Empresadetobjetivos.OBJETIVO4.value),
            rx.list.item(Empresadetobjetivos.OBJETIVO5.value),
            style=title_body_style
            ),
        imageninfo(imginfoo),
        rx.divider(),  
        ppadding= "10px",
        border=Size.ZERO,
        width="100%"    
)
