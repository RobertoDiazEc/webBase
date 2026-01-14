"""Common templates used between pages in the app."""

from __future__ import annotations

from .. import styles
from redx_web.components.sidebar import sidebar
from redx_web.components.navbar import navbar
from redx_web.components.footer import footer
from typing import Callable

import reflex as rx

preview = "/logoREDXWEB.png"

# Meta tags for the app.
default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1",
    },
    {"name": "og:type", "content": "website"},
    {"name": "og:imagen", "content": preview},
]


def menu_item_link(text, href):
    return rx.menu.item(
        rx.link(
            text,
            href=href,
            width="100%",
            color="inherit",
        ),
        _hover={
            "color": styles.accent_color,
            "background_color": styles.accent_text_color,
        },
    )


class ThemeState(rx.State):
    """The state for the theme of the app."""

    accent_color: str = "blue"

    gray_color: str = "gray"

    radius: str = "large"

    scaling: str = "100%"


""" def template(
    route: str | None = None,
    title: str | None = None,
    description: str | None = None,
    meta: str | None = None,
    script_tags: list[rx.Component] | None = None,
    on_load: rx.EventHandler | list[rx.EventHandler] | None = None,
    routeimagen: str | None = None """
def template(routeimagen: str | None = None) -> Callable[[Callable[[], rx.Component]], rx.Component]:
    """The template decorator for the app pages."""
    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        """The template for each page of the app.

        Args:
            page_content: The content of the page.

        Returns:
            The template with the page content.
        """
        # Get the meta tags for the page.
        #all_meta = [*default_meta, *(meta or [])]

        """ @rx.page(
            route=route,
            title=title,
            description=description,
            meta=all_meta,
            script_tags=script_tags,
            on_load=on_load,
           ) """
        
        def templated_page():
            return rx.box(
                navbar(),
                rx.divider(),
                # rx.box(
                #     rx.image(src=routeimagen, width="100%"),
                #     width="100%",
                #     width_max=["100%", "100%", "100%", "100%", "100%", styles.max_width],
                #     margin="auto",
                # ),
                # rx.vstack(
                #     rx.script(src="https://prod.spline.design/js/runtime.js"),
                #     rx.html(
                #         """
                #         <div style='width: 100%; height: 600px;'>
                #             <iframe 
                #                 src='https://my.spline.design/untitled-abc123xyz' 
                #                 width='100%' 
                #                 height='100%'
                #                 frameborder='0'
                #             ></iframe>
                #         </div>
                #         """
                #     )
                # ),
                rx.flex(
                    rx.vstack(
                        page_content(),
                        width="100%",
                        **styles.template_content_style,
                    ),
                    width="100%",
                    **styles.template_page_style,
                    max_width=[
                        "100%",
                        "100%",
                        "100%",
                        "100%",
                        "100%",
                        styles.max_width,
                    ],
                    flex_wrap="wrap",
                    justify="between",
                    flex_direction=["column", "column", "row"],

                ),
                footer(),
                
                
                width="100%",
                margin="auto",
                position="relative",
            )
       
       
           
        def theme_wrap():
            return rx.theme(
                templated_page(),
                has_background=True,
                accent_color=ThemeState.accent_color,
                gray_color=ThemeState.gray_color,
                radius=ThemeState.radius,
                scaling=ThemeState.scaling,
            )

        return theme_wrap

    return decorator
