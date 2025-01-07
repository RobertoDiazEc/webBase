"""Navbar component for the app."""

from .. import styles
from ..stylesRD.colors import Color
from ..ui.routes import Route

import reflex as rx


def menu_item_icon(icon: str) -> rx.Component:
    return rx.icon(icon, size=20)


def menu_item(text: str, url: str) -> rx.Component:
    """Menu item.

    Args:
        text: The text of the item.
        url: The URL of the item.

    Returns:
        rx.Component: The menu item component.
    """
    # Whether the item is active.
    active = (rx.State.router.page.path == url.lower()) | (
        (rx.State.router.page.path == Route.INDEX.value) & text == "Overview"
    )

    return rx.link(
        rx.hstack(
            rx.match(
                text,
                ("Dashboard", menu_item_icon("layout-dashboard")),
                ("About", menu_item_icon("book-open")),
                ("Settings", menu_item_icon("settings")),
                menu_item_icon("layout-dashboard"),
            ),
            rx.text(text, size="4", weight="regular"),
            color=rx.cond(
                active,
                styles.accent_text_color,
                styles.text_color,
            ),
            style={
                "_hover": {
                    "background_color": rx.cond(
                        active,
                        styles.accent_bg_color,
                        styles.gray_bg_color,
                    ),
                    "color": rx.cond(
                        active,
                        styles.accent_text_color,
                        styles.text_color,
                    ),
                    "opacity": "1",
                },
                "opacity": rx.cond(
                    active,
                    "1",
                    "0.95",
                ),
            },
            align="center",
            border_radius=styles.border_radius,
            width="100%",
            spacing="2",
            padding="0.35em",
        ),
        underline="none",
        href=url,
        width="100%",
    )


def navbar_footer() -> rx.Component:
    """Navbar footer.

    Returns:
        The navbar footer component.
    """
    return rx.hstack(
        rx.link(
            rx.text("Docs", size="3"),
            href="/",
            color_scheme="gray",
            underline="none",
        ),
        rx.link(
            rx.text("Blog", size="3"),
            href="/",
            color_scheme="gray",
            underline="none",
        ),
        rx.spacer(),
        rx.color_mode.button(style={"opacity": "0.8", "scale": "0.95"}),
        justify="start",
        align="center",
        width="100%",
        padding="0.35em",
    )


def menu_button() -> rx.Component:
    # Get all the decorated pages and add them to the menu.
    from reflex.page import get_decorated_pages

    # The ordered page routes.
    ordered_page_routes = [
        "/",
        "/about",
        "/settings",
    ]

    # Get the decorated pages.
    pages = get_decorated_pages()

    # Include all pages even if they are not in the ordered_page_routes.
    ordered_pages = sorted(
        pages,
        key=lambda page: (
            ordered_page_routes.index(page["route"])
            if page["route"] in ordered_page_routes
            else len(ordered_page_routes)
        ),
    )

    return rx.drawer.root(
        rx.drawer.trigger(
            rx.icon("align-justify"),
        ),
        rx.drawer.overlay(z_index="5"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.hstack(
                        rx.spacer(),
                        rx.drawer.close(rx.icon(tag="x")),
                        justify="end",
                        width="100%",
                    ),
                    rx.divider(),
                    *[
                        menu_item(
                            text=page.get(
                                "title", page["route"].strip("/").capitalize()
                            ),
                            url=page["route"],
                        )
                        for page in ordered_pages
                    ],
                    rx.spacer(),
                    navbar_footer(),
                    spacing="4",
                    width="100%",
                ),
                top="auto",
                left="auto",
                height="100%",
                width="20em",
                padding="1em",
                bg=rx.color("gray", 1),
            ),
            width="100%",
        ),
        direction="right",
    )


def navbar() -> rx.Component:
    """The navbar.

    Returns:
        The navbar component.
    """

    return rx.el.nav(
        rx.desktop_only(
            rx.hstack(
                # The logo.
                rx.link(
                    rx.hstack(
                    rx.image(src="/logoREDXWEB.png", height="2em",radius="large"),
                    rx.text("RED{x}Soluciones",
                            height="2em",
                            ),
                    ),
                    size="3",
                    href=Route.INDEX.value,
                ),            
                rx.spacer(),
                rx.link(
                        rx.hstack(
                        rx.icon("user-round-check", stroke_width=2),
                        rx.text("Registrate"),
                        ),
                        size="2",
                        href=Route.REGISTRATE.value,
                ), 
                rx.link(
                        rx.hstack(
                        rx.icon("phone-call", stroke_width=2),
                        rx.text("Contactanos"),
                        ),
                        size="2",
                        href=Route.CONTACTOS.value,
                ), 
            
                #menu_button(),
                align="center",
                width="100%",
                padding_y="1.15em",
                padding_x=["1em", "1em", "1em"],
            ),
        ),  
            
        rx.mobile_and_tablet(
                rx.hstack(
                    rx.hstack(
                        rx.link(
                            rx.hstack(
                            rx.image(src="/logoREDXWEB.png", height="2em",radius="large"),
                            rx.text("RED{x}Soluciones",
                                    height="2em",
                                    ),
                            ),
                            size="3",
                            href=Route.INDEX.value,
                        ), 
                        align_items="center",
                    ),
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.icon_button(
                                rx.icon("align-justify"),
                                size="2",
                                
                            )
                        ),
                        rx.menu.content(
                            rx.menu.item("Registrate"),
                            rx.menu.item(rx.link(
                                rx.text("Contactanos"),
                                size="2",
                                href=Route.CONTACTOS.value,
                                ),
                            ),
                            #rx.menu.separator(),
                            #rx.menu.item("Log out"),
                        ),
                        justify="end",
                    ),
                    justify="between",
                    align_items="center",
                ),
        ),         
        display=["block", "block", "block", "block", "block", "none"],
        #position="sticky",
        position="fixed",
         #display= "flex",
        bg=Color.NAVBAR_FOOTER.value,
        z_index="1000",
        width="100%",
        overflow="auto",  
        #background_color=Color.NAVBAR.value,
        border_bottom=styles.border,
    )
