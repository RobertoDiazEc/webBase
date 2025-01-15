import reflex as rx

import reflex_chakra as rc

from ...ui.routes import Route
from ...components.index_imagen import imageninfo




def serheaderedx(imginfo: str) -> rx.Component:
    return rx.fragment(
                    #rc.color_mode_button(rc.color_mode_icon(), float="right"),
                    rx.hstack(
                        rx.flex(
    
                            rc.vstack(
                                    rc.heading("TE DAMOS LA BIENVENIDA!", font_size="2em"),
                                    rc.center("REDx Soluciones es el aliado perfecto que estabas buscando en el desarrollo y soporte tecnológico. Brindamos Soluciones en tiempos reales, mejoramos procesos, reducimos costos."),
                                    rc.center("Desarrollo de Software a Medida"), 
                                    rc.center("Soporte Técnico 24/7"), 
                                    rc.center("Consultoría en TI"),
                                    
                                    rc.link(
                                        rx.hstack(
                                        rx.icon("user-round-check", stroke_width=2),
                                        "Contactanos", ),
                                        href=Route.CONTACTOS.value,
                                    ),   
                                    spacing="1em",
                                    padding="5%",
                                ),
                            imageninfo(imginfo),
                            flex_direction=["column","row"]
                        ),  
                    
                    #padding_top="10%", 
                    width="100%",
                    ), 
                ),

def sersomosredx(imginfo: str) -> rx.Component:
    return rx.fragment(
                    #rc.color_mode_button(rc.color_mode_icon(), float="right"),
            rx.hstack(
                rx.flex(
                    rc.vstack(
                        rc.heading("Quienes somos"),
                        rc.center("mi nombre es Roberto Diaz, soy Desarrollador de Sistemas por mas de 15 años en area de produccion, facturacion, bodega, contabilidad, integracion, implementacion de modelos personalizados."),
                        rc.center("Desarrollamos aplicaciones web, móviles y de escritorio utilizando tecnologías como Visual, C+, Python, Reflex, JavaScript, PHP, y más."),
                        rc.center("Ofrecemos soporte técnico 24/7 para resolver cualquier problema tecnológico rápidamente."),
                        rc.center("Ayudamos a tu empresa a optimizar su infraestructura tecnológica y fortalecer su ciberseguridad."),
                        spacing="1em",
                        padding="5%", 
                    ),
                    imageninfo(imginfo),
                    #padding_top="10%",
                    flex_direction=["column","row"]
                ),    
                width="100%", 

            ),
        ),


def serserviciosredx(titulo: str, detalle: str, imginfo: str, colorsi: bool) -> rx.Component:
    return rx.fragment(
                    #rc.color_mode_button(rc.color_mode_icon(), float="right"),
             
            rx.card(
                    rx.link(
                    rx.hstack(
                        
                        rc.vstack(
                            imageninfo(imginfo),
                            rc.heading(titulo),
                            rc.center(detalle),
                         
                           spacing="1em",
                           padding="5%", 
                        ),
                        width="100%",
                    ),
                ),
                size="3",
                background_color= rx.cond(
                    colorsi,            
                    "#f4ea43", 
                    "#246c85",
                    ),
                width="100%"    
            ),
           

     )

def serautomatizacionredx(titulo: str, detalle: str, icoinfo: str, colorsi: bool) -> rx.Component:
    return rx.fragment(
                    #rc.color_mode_button(rc.color_mode_icon(), float="right"),
             
            rx.card(
                    
                rx.hstack(
                    rx.icon(icoinfo,size=125),
                    rc.vstack(
                        rc.heading(titulo),
                        rc.center(detalle),
                        
                        spacing="1em",
                        padding="5%", 
                    ),                    
                ),
                size="3",
                background_color= rx.cond(
                    colorsi,            
                    "#096df9", 
                    "#246c85",
                    ),
                width="100%"    
            ),
           

     )
