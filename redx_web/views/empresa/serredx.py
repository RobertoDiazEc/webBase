import reflex as rx

from ...ui.routes import Route
from ...components.index_imagen import imageninfo




def serheaderedx(imginfo: str) -> rx.Component:
    return rx.fragment(
                    #rc.color_mode_button(rc.color_mode_icon(), float="right"),
        rx.box(
                    rx.hstack(
                        rx.flex(

                            rx.vstack(
                                    rx.heading("Transformamos ideas en impacto", font_size=["1em", "2em", "3em"],
                                                color="#0A0A0AFF",
                                                padding_bottom="2%"
                                                ),
                                    rx.divider(border_color="white"),                                                
                                    rx.center("No se trata solo de lo que hacemos, sino de cómo lo cambia todo. Explora la diferencia que una solución tecnológica bien diseñada puede hacer para tu negocio.", 
                                              color="#0A0A0AF0"
                                              ),
                                    rx.center("Tu próximo paso comienza aquí. Descubre qué es posible cuando la tecnología encuentra el propósito.",
                                        color="#0A0A0AF0"), 
                                    rx.center("Diseñamos, construimos y mantenemos la tecnología que tu negocio necesita para seguir creciendo.", color="#0A0A0AF0"), 
                                    rx.center("Acompañamos cada etapa de tu negocio con tecnología estable, escalable y pensada para ti.", color="#0A0A0AF0"    ),

                                    rx.link(
                                        rx.hstack(
                                        rx.icon("user-round-check", stroke_width=2),
                                        "Contactanos", ),
                                        href=Route.CONTACTOS.value,
                                        font_size="1.5em",
                                        color="#860E0EDC",
                                        padding_top="2%",
                                        justify_content="center",
                                    ),   
                                    spacing="2",
                                    padding="5%",
                                ),
                            imageninfo(imginfo),
                            flex_direction=["column","row","row","row","row","row"],
                        ),  
                    
                    #padding_top="10%", 
                    width="100%",
                    ), 
        background_color="#edf1f3ff",
        padding_bottom="2%",
        ),
  ),

def sersomosredx(imginfo: str) -> rx.Component:
    return rx.fragment(
                    #rc.color_mode_button(rc.color_mode_icon(), float="right"),
        rx.box(            
            rx.hstack(
                rx.flex(
                    rx.vstack(
                        rx.heading("Quienes somos",
                                    font_size=["1em", "2em", "3em"],
                                    color="#0f0f0fff",
                                    padding_bottom="2%"
                                    ),
                        rx.divider(border_color="white"),
                        rx.center("mi nombre es Roberto Diaz, soy Desarrollador de Sistemas por mas de 15 años en area de produccion, facturacion, bodega, contabilidad, integracion, implementacion de modelos personalizados.", color="#0f0f0fd8"),
                        rx.center("Desarrollamos aplicaciones web, móviles y de escritorio utilizando tecnologías como Visual, C+, Python, Reflex, JavaScript, PHP, y más.", color="#0f0f0fd8"),
                        rx.center("Ofrecemos soporte técnico 24/7 para resolver cualquier problema tecnológico rápidamente.", color="#0f0f0fd8"),
                        rx.center("Ayudamos a tu empresa a optimizar su infraestructura tecnológica y fortalecer su ciberseguridad.", color="#0f0f0fd8"),
                        spacing="2",
                        padding="5%", 
                    ),
                    imageninfo(imginfo),
                    #padding_top="10%",
                    flex_direction=["column","row","row","row","row","row"],
                ),    
                width="100%", 

            ),
            background_color="#edf1f3ff",
            padding_bottom="2%",    
        ),
    ),


def serserviciosredx(titulo: str, detalle: str, imginfo: str, colorsi: bool) -> rx.Component:
    return rx.fragment(
                    #rc.color_mode_button(rc.color_mode_icon(), float="right"),
        rx.box(
            rx.card(
                    rx.link(
                    rx.hstack(
                        
                        rx.vstack(
                            imageninfo(imginfo),
                            rx.heading(titulo),
                            rx.center(detalle),
                         
                           spacing="1",
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
            padding_bottom="2%",    
        ),  

     )

def serautomatizacionredx(titulo: str, detalle: str, icoinfo: str, colorsi: bool) -> rx.Component:
    return rx.fragment(
                    #rc.color_mode_button(rc.color_mode_icon(), float="right"),
             
            rx.card(
                    
                rx.hstack(
                    rx.icon(icoinfo,size=125),
                    rx.vstack(
                        rx.heading(titulo),
                        rx.center(detalle),
                        
                        spacing="1",
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
