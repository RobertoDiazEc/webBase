import reflex as rx
import time 
from typing import Union, List
import csv

from redx_web.api.api import api_usuarios
from ..model.userweb import ItemUsu
       

#self.items = [ItemUsu(**row) for row in api_usuarios]
""" data = await api_usuarios()
         print(data) """

class PageState(rx.State):

    items: list[ItemUsu]
   
    async def  usuarios_dataweb(self):  
        self.items = await api_usuarios()
