import reflex as rx

import ..styles.styles as style

def header_base(srcimagen: str) -> rx.Component:
    return rx.box( 
          rx.image(
                src=srcimagen, 
                width="100%", 
                height="50%",
                auto="format",
                ),
            position= "relative",
            width="100%"
    )       