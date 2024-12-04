import reflex as rx
import ..styles.styles as styles

def link_button_wharsaap(text: str, url: str, iconom: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag=iconom,
                ),
                rx.text(text, style=styles.button_title_style)
            ),
        color_scheme="green",
        ),
        href=url,
        is_external=True,
        width="100%",
        
    )