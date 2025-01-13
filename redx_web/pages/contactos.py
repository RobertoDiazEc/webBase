"""The dashboard page."""
import reflex as rx
import time 
from ..templates import template
from ..styles import button_title_style
from ..constants import WHATSAPP_URL
from redx_web.api.api import api_contactos_crear




class contactosState(rx.State):
    
    form_data: dict = {}
    enviado_data: bool = False
    nombre_data: str = ""
    nombre_get: str = ""
    activo: bool = True
    unificar: str = ""
    
    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        #print(form_data)
        self.form_data = form_data
        self.enviado_data = True
        self.nombre_get= form_data.get("nombre") or ""
        self.activo= False
        self.unificar = await api_contactos_crear(self.form_data)
        yield
        time.sleep(2)
        self.enviado_data = False
        yield

            




@rx.page(route="/contactos", title="Contactos")
@template(routeimagen="")
def contactos() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.container(
        rx.flex(
                
            rx.vstack(
                rx.heading("CONTACTANOS", 
                    size="8",
                    padding_top="10%"
                    ),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Nombre",
                        name="nombre",
                        type="text",
                        required=True,
                        width="100%"
                    ),
                    rx.input(
                        placeholder="Apellido", 
                        name="apellido",
                        type="text",
                        required=True,
                        width="100%"
                    ),
                    rx.input(
                        placeholder="Email",
                        type="email",
                        name="email",
                        required=True,
                        width="100%"
                    ),
                    rx.input(
                        placeholder="Celular",
                        type="int",
                        name="celular",
                        required=True,
                        width="100%"
                    ),
                    rx.text_area(
                        placeholder="Tu Mensaje", 
                        name="mensaje",
                        required=True,
                        width="100%"
                    ),
                    rx.button("Enviar", 
                              desabled= contactosState.activo),
                    spacing="4",
                    width="100%",   
                    ),
                on_submit= contactosState.handle_submit,
                reset_on_submit=True,
                
                ),
                rx.divider(),
                rx.cond(contactosState.enviado_data, 
                        f"Gracias por escribirnos {contactosState.nombre_get}",
                        ""),

            spacing="4",
            width="100%",
            padding="25px 25px",
            ),
            rx.flex(
                rx.heading(
                    "Whatsapp",
                    size="8",
                    padding_top="25%"
                ),
                rx.link(
                    rx.button(
                        rx.hstack(
                            rx.icon(
                                tag="message-circle-more",
                            ),
                            rx.text("Escribenos", style=button_title_style)
                        ),
                        color_scheme="green",
                    ),
                    href=WHATSAPP_URL,
                    is_external=True,
                    width="100%",
                ),
                spacing="2",
                text_align=["center", "center", "start"],
                flex_direction="column",
            ),
            justify="between",
            spacing="6",
            flex_direction=["column", "column", "row"],
            width="100%",
        ),
        padding="25px 25px",
        width="100%",
)
