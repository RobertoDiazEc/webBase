"""Welcome to Reflex!."""

# Import all the pages.
from .pages import *
from . import styles
import reflex as rx


# Create the app.
app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
)

#app.api.add_api_route("/repo", repo)