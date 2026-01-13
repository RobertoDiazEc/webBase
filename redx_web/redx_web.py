"""Welcome to Reflex!."""

# Import all the pages.
from redx_web.pages.redx_inicio import redx_inicio

from redx_web import styles
import reflex as rx


# Create the app.
app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
)

app.add_page(
    redx_inicio,
)