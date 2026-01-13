
from ..empresa.serredx import serserviciosredx, serautomatizacionredx
import reflex as rx



def serviciosredx() -> rx.Component:
    return  rx.vstack(
                    rx.heading("SERVICIOS", 
                               size="6",
                               align="center",
                               width="100%",
                               color="#f8f5f5ff"),
                    rx.flex(
                        serserviciosredx(
                            "Desarrollo Aplicaciones",
                            "nos acoplamos a tu presupuesto",
                            "/imagenes/programacion2.png",
                            False,
                        ),
                        
                        serserviciosredx(
                            "Desarrollo Web",
                            "Pagina Web desde $ 100, visualiza tu emprendimiento",
                            "/imagenes/programacion4.png",
                            True,
                        ),
                        serserviciosredx(
                            "Soporte 24/7",
                            "Mantenimiento de Equipos, Actualizacion, Reparacion",
                            "/imagenes/programacion3.png",
                            False,
                        ),
                       
                        spacing="2",
                    
                        flex_direction=["column","row"],
                        ),
                   
                #min_height="85vh",
                width="100%",    
        )
       

def productosredx() -> rx.Component:
    return rx.hstack(
                rx.flex(
                        serserviciosredx(
                            "Venta de Equipos",
                            "nos acoplamos a tu presupuesto",
                            "/imagenes/programacion2.png",
                            False,
                        ),
                        
                        serserviciosredx(
                            "Nivelacion Continua",
                            "nos acoplamos a tu presupuesto",
                            "/imagenes/programacion4.png",
                            False,
                        ),
                        serserviciosredx(
                            "Servicio Tecnico",
                            "Mantenimiento de Equipos, Actualizacion, Reparacion",
                            "/imagenes/programacion3.png",
                            False,
                        ),
                    spacing="2",
                    flex_direction=["column","row"],   
                    ),
                    
    ),


def automatizacionredx() -> rx.Component:
    return  rx.vstack(
                    
                    rx.heading("AUTOMATIZACION", 
                               size="6",
                               align="center",
                               width="100%",
                               color="#f8f5f5ff"),
                  
                    serautomatizacionredx(
                            "Convertir Facturas PDFs a datos para tu Base de Datos",
                            "Proceso para leer las FACTURAS PDF y transformarlos en datos para su registro, en un Excel o base de datos",
                            "building-2",
                            False,
                        ),
                   
                #min_height="85vh",
                width="100%",    
        )
 
                        