import reflex as rx
from ..styles.styles import styles
from ..styles.styles import Size

def title( text: str) -> rx.Component:
    return rx.heading(
        text,
        size=Size.LARGE.value,
        style=styles.title_style

    )
