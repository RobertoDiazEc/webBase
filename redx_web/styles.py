"""Styles for the app."""

import reflex as rx

from enum import Enum
from .stylesRD.colors import Color as Color
from .stylesRD.colors import TextoColor as TextColor
from .stylesRD.fonts import Font, FontWeight


border_radius = "var(--radius-2)"
border = f"1px solid {rx.color('gray', 5)}"
text_color = rx.color("gray", 11)
gray_color = rx.color("gray", 11)
gray_bg_color = rx.color("gray", 3)
accent_text_color = rx.color("accent", 10)
accent_color = rx.color("accent", 1)
accent_bg_color = rx.color("accent", 3)
hover_accent_color = {"_hover": {"color": accent_text_color}}
hover_accent_bg = {"_hover": {"background_color": accent_color}}
content_width_vw = "90vw"
sidebar_width = "32em"
sidebar_content_width = "16em"
max_width = "1480px"
color_box_size = ["2.25rem", "2.25rem", "2.5rem"]


template_page_style = {
    "padding_top": ["1em", "1em", "2em"],
    "padding_x": ["auto", "auto", "2em"],
}

template_content_style = {
    "padding": "1em",
    "margin_bottom": "2em",
    "min_height": "90vh",
}

link_style = {
    "color": accent_text_color,
    "text_decoration": "none",
    **hover_accent_color,
}

overlapping_button_style = {
    "background_color": "white",
    "border_radius": border_radius,
}

markdown_style = {
    "code": lambda text: rx.code(text, color_scheme="gray"),
    "codeblock": lambda text, **props: rx.code_block(text, **props, margin_y="1em"),
    "a": lambda text, **props: rx.link(
        text,
        **props,
        font_weight="bold",
        text_decoration="underline",
        text_decoration_color=accent_text_color,
    ),
}

box_shadow_style = "0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)"

color_picker_style = {
    "border_radius": "max(var(--radius-3), var(--radius-full))",
    "box_shadow": box_shadow_style,
    "cursor": "pointer",
    "display": "flex",
    "align_items": "center",
    "justify_content": "center",
    "transition": "transform 0.15s ease-in-out",
    "_active": {
        "transform": "translateY(2px) scale(0.95)",
    },
}


# Constantes
MAX_WIDTH = "560px"
MED_WIDTH = "300px"
MIN_WIDTH = "100px"


#fond sheets

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght500&display=swap"
]

# Sizes
class Size(Enum):
    ZERO = "0em"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    BIGN1 ="3em"

# Botton
# "font_family": Font.DEFAULT.value,
# "font_weight": Font
BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,    
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "_hover": {
            "background_color": Color.SECONDARY.value
        }
    },
    rx.link: {
        "text_decoration" : "none",
        "_hover" : {
             #"background_color": Color.SECONDARY.value,
             "background_color": Color.CONTENT.value,
            "color": Color.PRIMARY.value,
        }
    }
}

title_style=dict(
    width="100%",
    padding_top=Size.MEDIUM.value,
    padding=Size.MEDIUM.value,
    color=TextColor.HEADER.value,
    
)

title_header_style=dict(
    width="100%",
    color=Color.BACKGROUND.value
)

title_body_style=dict(
    width="100%",
    padding="1em",
    color=TextColor.BODY.value
)

button_title_style = dict(
    font_size = Size.DEFAULT.value,
    color=TextColor.HEADER.value
)

button_body_style = dict(
    font_size = Size.SMALL.value
)

# Common styles for questions and answers.
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="30em",
    display="inline-block",
)



base_navbar = dict( 
    position= 'fixed', 
    top= '0',
    widt= '100%',
    transition= 'background-color 0.3s ease',
)

base_navbar_transparent = dict( 
    background_color= 'rgba(255, 255, 255, 0)',
) 

base_navbar_dark= dict ( 
    background_color= 'rgba(0, 0, 0, 0.8)',
)