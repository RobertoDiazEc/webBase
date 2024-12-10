from ..templates import template
from .. import styles
import reflex as rx
import reflex_chakra as rc

#@require_login

@rx.page(route="/protected", title="REDx Soluciones")
@template(routeimagen="/imagenes/portadaRedx1.jpg")
def protected() -> rx.Component:
    """Render a protected page.

    The `require_login` decorator will redirect to the login page if the user is
    not authenticated.

    Returns:
        A reflex component.
    """
    return rx.container(
    rx.box(
        rx.flex(
            rx.box(
                rx.image(
                    src="/logoREDXWEB.png",
                    alt="REDx Soluciones Informatica",
                    height="2.5rem",
                    margin_left="auto",
                    margin_right="auto",
                    width="auto",
                ),
                rx.heading(
                    "Inicia sesión en tu cuenta",
                    class_name="text-2xl/9",
                    font_weight="700",
                    margin_top="2.5rem",
                    text_align="center",
                    color="#111827",
                    letter_spacing="-0.025em",
                    as_="h2",
                    size="6",
                ),
                max_width=rx.breakpoints({"640px": "24rem"}),
                margin_left=rx.breakpoints({"640px": "auto"}),
                margin_right=rx.breakpoints({"640px": "auto"}),
                width=rx.breakpoints({"640px": "100%"}),
            ),
            rx.box(
                rx.form(
                    rx.box(
                        rx.el.label(
                            "Email address",
                            class_name="text-sm/6",
                            display="block",
                            font_weight="500",
                            color="#111827",
                        ),
                        rx.box(
                            rx.el.input(
                                type="email",
                                name="email",
                                id="email",
                                autocomplete="email",
                                required=True,
                                class_name="-outline-offset-1 focus:-outline-offset-2 focus:outline focus:outline-indigo-600 outline outline-gray-300 placeholder:text-gray-400 sm:text-sm/6",
                                background_color="#ffffff",
                                display="block",
                                _focus={"outline-width": "2px"},
                                outline_width="1px",
                                padding_left="0.75rem",
                                padding_right="0.75rem",
                                padding_top="0.375rem",
                                padding_bottom="0.375rem",
                                border_radius="0.375rem",
                                font_size="1rem",
                                line_height="1.5rem",
                                color="#111827",
                                width="100%",
                            ),
                            margin_top="0.5rem",
                        ),
                    ),
                    rx.box(
                        rx.flex(
                            rx.el.label(
                                "Password",
                                class_name="text-sm/6",
                                display="block",
                                font_weight="500",
                                color="#111827",
                            ),
                            rx.box(
                                rx.el.a(
                                    "Forgot password?",
                                    href="#",
                                    font_weight="600",
                                    _hover={"color": "#6366F1"},
                                    color="#4F46E5",
                                ),
                                font_size="0.875rem",
                                line_height="1.25rem",
                            ),
                            display="flex",
                            align_items="center",
                            justify_content="space-between",
                        ),
                        rx.box(
                            rx.el.input(
                                type="password",
                                name="password",
                                id="password",
                                autocomplete="current-password",
                                required=True,
                                class_name="-outline-offset-1 focus:-outline-offset-2 focus:outline focus:outline-indigo-600 outline outline-gray-300 placeholder:text-gray-400 sm:text-sm/6",
                                background_color="#ffffff",
                                display="block",
                                _focus={"outline-width": "2px"},
                                outline_width="1px",
                                padding_left="0.75rem",
                                padding_right="0.75rem",
                                padding_top="0.375rem",
                                padding_bottom="0.375rem",
                                border_radius="0.375rem",
                                font_size="1rem",
                                line_height="1.5rem",
                                color="#111827",
                                width="100%",
                            ),
                            margin_top="0.5rem",
                        ),
                    ),
                    rx.box(
                        rx.el.button(
                            "Sign in",
                            type="submit",
                            class_name="focus-visible:outline focus-visible:outline-2 focus-visible:outline-indigo-600 focus-visible:outline-offset-2 text-sm/6",
                            background_color="#4F46E5",
                            display="flex",
                            font_weight="600",
                            _hover={"background-color": "#6366F1"},
                            justify_content="center",
                            padding_left="0.75rem",
                            padding_right="0.75rem",
                            padding_top="0.375rem",
                            padding_bottom="0.375rem",
                            border_radius="0.375rem",
                            box_shadow="0 1px 2px 0 rgba(0, 0, 0, 0.05)",
                            color="#ffffff",
                            width="100%",
                        )
                    ),
                    action="#",
                    method="POST",
                    display="flex",
                    flex_direction="column",
                    gap="1.5rem",
                ),
                rx.text(
                    " Not a member? ",
                    rx.el.a(
                        "Start a 14 day free trial",
                        href="#",
                        font_weight="600",
                        _hover={"color": "#6366F1"},
                        color="#4F46E5",
                    ),
                    class_name="text-sm/6",
                    margin_top="2.5rem",
                    text_align="center",
                    color="#6B7280",
                ),
                margin_top="2.5rem",
                max_width=rx.breakpoints({"640px": "24rem"}),
                margin_left=rx.breakpoints({"640px": "auto"}),
                margin_right=rx.breakpoints({"640px": "auto"}),
                width=rx.breakpoints({"640px": "100%"}),
            ),
            display="flex",
            flex_direction="column",
            justify_content="center",
            min_height="100%",
            padding_left=rx.breakpoints({"0px": "1.5rem", "1024px": "2rem"}),
            padding_right=rx.breakpoints({"0px": "1.5rem", "1024px": "2rem"}),
            padding_top="3rem",
            padding_bottom="3rem",
        ),
    ),
    position="absolute", 
            top= "15%", 
            left= "50%", 
            transform= "translate(-50%, -50%)", 
            color= "white", 
            font_size= "24px", 
            font_weight= "bold", 
            background_color= "rgba(0, 0, 0, 1.5)", 
            padding="10px", 
            border_radius= "5px" ,  
)