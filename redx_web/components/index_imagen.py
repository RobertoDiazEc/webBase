import reflex as rx


def imageninfo( imginfo: str) -> rx.Component:
    if imginfo=="":
        return rx.box()
    else: 
        return rx.container(
        rx.center( 
            rx.image(
                src=imginfo, 
                width="80%", 
                height="auto",
                #auto="format",
                margin="10px",
                border_radius="15px 15px",
                border="1px solid #217F4F",                
                ),
               
            ), 
        size="1",
        padding= "10px 10px",
        margin="10px 10px",
    )

