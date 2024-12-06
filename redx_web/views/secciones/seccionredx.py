
from ..empresa.serredx import serserviciosredx
import reflex as rx



def serviciosredx() -> rx.Component:
    return rx.flex(
                    rx.hstack(
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
                    ),
                    spacing="2",
                    align_items="flex-start",
                    flex_wrap="wrap"
        ),



def productosredx() -> rx.Component:
    return rx.flex(
                    rx.hstack(
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
                    ),
                    spacing="2",
                    align_items="flex-start",
                    flex_wrap="wrap"
    ),