import reflex as rx
import ..styles.styles as styles

def link_button(text: str, url: str, iconom: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag=iconom,
                ),
                rx.text(text, style=styles.button_title_style)
            )
        ),
        href=url,
        is_external=True,
        width="100%"
  
    )