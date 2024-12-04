import reflex as rx
import ..styles.styles as styles

def imageninfo( imginfo: str) -> rx.Component:
    if imginfo=="":
        return rx.box()
    else: 
        return rx.box(
        rx.center( 
            rx.image(
                src=imginfo, 
                width="70%", 
                height="auto",
                #auto="format",
                margin="10px",
                border_radius="15px 50px",
                border="2px solid #217F4F",
                ),
               
            ), 
        padding= "10px 10px",
    )

