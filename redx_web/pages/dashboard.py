"""The dashboard page."""

from ..templates import template
from ..backend.table_state import TableState
from ..views.table import main_table

import reflex as rx
import reflex_chakra as rc

@template(route="/Dashboard", title="Dashboard", on_load=TableState.load_entries)
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
       # rx.heading("CI Job Dashboard", size="5"),
       # main_table(),
        rc.heading("This is a header"),
        rc.center("This text is centered"),
        rc.button(
               "click me",
               on_click=rx.toast("show toast!"),
               bg="purple",
               border_radius="0.5em",
               pl="10px"
           ),
   
        spacing="8",
        width="100%",
    )
