"""The dashboard page."""
import time 
from ..templates import template

from ..api.api import api_contactos_crear
import reflex as rx



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
        print(form_data)
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
            width="50%",
            padding="25px 25px",
        ),
        padding="25px 25px",
        width="100%",
)
