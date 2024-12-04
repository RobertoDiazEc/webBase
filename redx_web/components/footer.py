import reflex as rx

from ..stylesRD.fonts import FontSize
from ..styles import title_style
from ..stylesRD.colors import Color

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="2", font_size= FontSize.FOOTER.value), href=href)


def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading(
            "PRODUCTOS", 
            style=title_style
        ),
        footer_item("Venta de Equipos", "/#"),
        footer_item("Mantenimientos", "/#"),
        footer_item("E-commerce", "/#"),
        spacing="2",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading(
            "SERVICIOS", style=title_style
        ),
        footer_item("Sistemas Personalizados", "/#"),
        footer_item("Aplicaciones", "/#"),
        footer_item("Desarrollo Web", "/#"),
        spacing="2",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )

def footer_items_3() -> rx.Component:
    return rx.flex(
        rx.heading(
            "CONTACTOS", 
            style=title_style
        ),
        footer_item("Email: contacto@redxsolucion.com", "/#"),
        footer_item("Mobil: +593 985713144", "/#"),
        footer_item("QUITO - ECUADOR", "/#"),
       
        #footer_item("E-commerce", "/#"),
        spacing="2",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )

def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        social_link("linkedin", "/#"),
        spacing="3",
        justify="end",
        width="100%",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.divider(),
            rx.flex(
                rx.vstack(
                    
                rx.hstack(
                    rx.link(
                        rx.hstack(
                            rx.image(
                                src="/logoREDXWEB.png",
                                width="4em",
                                height="auto",
                                border_radius="50%",
                            ),
                            rx.heading(
                                "Tecnologia a tu Alcance ", 
                            size="5", 
                            weight="bold",
                            #color= Color.CONTENT.value
                            ),
                        ),
                        href="/"
                    ),
                    
                    align_items="center",
                ),
                rx.text("© 2024",
                            size="2",
                            weight="bold",
                            ),
                spacing="4",
                align_items=[
                    "center",
                    "center",
                    "start",
                ],
                ),
                footer_items_3(),
                footer_items_1(),
                footer_items_2(),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            rx.divider(),
            rx.hstack(
                rx.hstack(
                    footer_item("Privacy Policy", "/#"),
                    footer_item("Terms of Service", "/#"),
                    footer_item("Developer: REDx Soluciones", "/#"),
                    spacing="6",
                    align="center",
                    width="100%",
                ),
                socials(),
                justify="between",
                width="100%",
            ),
            rx.divider(),
            spacing="5",
            width="100%",
        ),
        width="100%",
        bg=Color.NAVBAR_FOOTER.value,
    )