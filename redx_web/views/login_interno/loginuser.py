import reflex as rx

def dialogologin() -> rx.Component:
    return rx.dialog.root(
            rx.dialog.trigger(rx.button("Edit Profile", size="4")),
                rx.dialog.content(
                    rx.dialog.title("Edit Profile"),
                    rx.dialog.description(
                        "Change your profile details and preferences.",
                        size="2",
                        margin_bottom="16px",
                    ),
                    rx.flex(
                        rx.text(
                            "Nombre",
                            as_="div",
                            size="2",
                            margin_bottom="4px",
                            weight="bold",
                        ),
                        rx.input(
                            default_value="Roberto Diaz",
                            placeholder="Enter your name",
                        ),
                        rx.text(
                            "Email",
                            as_="div",
                            size="2",
                            margin_bottom="4px",
                            weight="bold",
                        ),
                        rx.input(
                            default_value="robertodiazec@gmail.com",
                            placeholder="Enter your email",
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                color_scheme="gray",
                                variant="soft",
                            ),
                        ),
                        rx.dialog.close(
                            rx.button("Save"),
                        ),
                        spacing="3",
                        margin_top="16px",
                        justify="end",
                    ),
                ),
        )