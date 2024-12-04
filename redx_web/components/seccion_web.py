import reflex as rx
import ..styles.styles as styles


def seccion_web(imgavatar: str, titulo: str, pie: str, url: str) -> rx.Component:
    return rx.box(
                rx.link(
                    rx.flex(
                        rx.icon(tag=imgavatar, size=35),
                        #rx.avatar(src=imgavatar),
                        rx.box(
                            rx.heading(titulo),
                            rx.text(pie ),
                           
                        ),
                        spacing="2",
                    ),
                    #color_scheme="blue",
                    #background= "gray" ,
                    href=url,
                ),
        as_child=True,
        padding= "5px",
        border=styles.Size.ZERO,
        width="100%"
    )
   