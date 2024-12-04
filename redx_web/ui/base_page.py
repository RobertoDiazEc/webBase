
import reflex as rx

from ..components.navbar import navbar
from ..components.footer import footer

import ..styles.styles as styles




def base_page(child: rx.Component, hide_navbar=False, *args, **kwargs) -> rx.Component:
    #print([type(x) for x in args])
        if hide_navbar:
                return rx.box(
                
                child,
                rx.color_mode.button(position="bottom-left", id='mi-color-modelo-btn'),
                footer(),
                id="mi-box-base",
                
            )
        else:
            return rx.box(
                navbar(),
                child,
                rx.color_mode.button(position="bottom-left", id='mi-color-modelo-btn'),
                footer(),
                id="mi-box-base",
                
            )    
