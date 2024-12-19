import reflex as rx
import time 
from typing import Union, List
import csv

from redx_web.api.api import api_usuarios
from ..model.userweb import ItemUsu

class insertContac(contactosState):
    nombre_data1: dict = {}
    unificar: str = ""
    
    @rx.event
    async def enviar_datos(self):
        self.nombre_data1 = self.form_data
        self.unificar = await api_usuarios_crear()
        print(self.unificar)
        self.unificar = await api_contactos_crear(self.form_data)
        print(self.unificar)

