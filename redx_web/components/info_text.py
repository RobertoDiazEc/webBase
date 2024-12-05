import reflex as rx
from ..stylesRD.stylespag import Size as Size


def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.span(title, font_weigth="bold", color="blue"),
        f" {body}", font_size=Size.MEDIUM.value
    )