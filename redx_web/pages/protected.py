from ..templates import template
from .. import styles
import reflex as rx
import reflex_chakra as rc

#@require_login
@template(route="/protected", title="REDx Soluciones",routeimagen="/imagenes/portadaRedx1.jpg")
def protected() -> rx.Component:
    """Render a protected page.

    The `require_login` decorator will redirect to the login page if the user is
    not authenticated.

    Returns:
        A reflex component.
    """
    return rc.vstack(
        rc.heading(
            "Protected Page for ", font_size="2em"
        ),
        rc.link("Home", href="/"),
        rc.link("Logout", href="/"),
    )