import reflex as rx


def usuario_nuevo() -> rx.Component:
    return rx.dialog.root(
            rx.dialog.trigger(rx.button("cerrar")),
            rx.dialog.content(
                rx.dialog.title("Gracias por escribirnos"),
                rx.dialog.description(
                    "estaremos gustoso de responder tus inquietudes"
                ),
                rx.dialog.close(
                    rx.button("Close Dialog", size="3"),
                ),
            ),
            #on_open_change="",
        )