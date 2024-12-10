
import reflex as rx
from ..backend.page_state import PageState, ItemUsu
from ..model.userweb import ItemUsu

def _show_item(item: ItemUsu, index: int) -> rx.Component:
    bg_color = rx.cond(
        index % 2 == 0,
        rx.color("gray", 1),
        rx.color("accent", 2),
    )
    hover_color = rx.cond(
        index % 2 == 0,
        rx.color("gray", 3),
        rx.color("accent", 3),
    )
    return rx.table.row(
        rx.table.row_header_cell(item.nombre),
        rx.table.cell(item.email),
        
        style={"_hover": {"bg": hover_color}, "bg": bg_color},
        align="center",
    )

def usuarioswebapi() -> rx.Component:
    return rx.flex(
        rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell(
                        "Usuarios"
                    ),
                    rx.table.column_header_cell(
                        "Correo"
                    ),
                   
                ),
            ),
            rx.table.body(
     
                rx.foreach(
                    PageState.items,
                    lambda items, index: _show_item(items, index),
                )
            ),
               
                
           
            width="100%",
        ),
       
    )            
)