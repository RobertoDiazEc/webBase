import reflex as rx
import ..styles.styles as styles

def seccion_title( titulo: str) -> rx.Component:
    return rx.box(
        rx.heading(titulo),
        padding= "10px",
        border=styles.Size.ZERO,
        width="100%"
    )