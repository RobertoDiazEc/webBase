
from ..empresa.serredx import serserviciosredx
import reflex as rx



def serviciosredx() -> rx.Component:
    return rx.hstack(
                    rx.flex(
                        serserviciosredx(
                            "Desarrollo de Aplicaciones",
                            "nos acoplamos a tu presupuesto",
                            "/imagenes/programacion2.png",

                        ),
                        
                        serserviciosredx(
                            "Desarrollo Web",
                            "nos acoplamos a tu presupuesto",
                            "/imagenes/programacion4.png",

                        ),
                        serserviciosredx(
                            "Soporte 24/7",
                            "Mantenimiento de Equipos, Actualizacion, Reparacion",
                            "/imagenes/programacion3.png",

                        ),
                        spacing="2",
                    
                        flex_direction=["column","row"],
                    ),
                    
        ),



def productosredx() -> rx.Component:
    return rx.hstack(
                rx.flex(
                        serserviciosredx(
                            "Venta de Equipos",
                            "nos acoplamos a tu presupuesto",
                            "/imagenes/programacion2.png",

                        ),
                        
                        serserviciosredx(
                            "Nivelacion Continua",
                            "nos acoplamos a tu presupuesto",
                            "/imagenes/programacion4.png",

                        ),
                        serserviciosredx(
                            "Servicio Tecnico",
                            "Mantenimiento de Equipos, Actualizacion, Reparacion",
                            "/imagenes/programacion3.png",

                        ),
                    spacing="2",
                    flex_direction=["column","row"],   
                    ),
                    
    ),