import reflex as rx
from ..components.header_button import header_button
import ..constants  as Constants

def button_header() -> rx.Component:
    return rx.vstack(
        header_button("CPK", "COSTO POR KILOMETRO"),
        
    )
