
from .Supabase_api import Supabase_API
from ..model.userweb import ItemUsu

SUPABASE_API = Supabase_API()

async def api_usuarios() -> list[ItemUsu]:
    return SUPABASE_API.Usuario_ApiBase()

async def api_usuarios_crear():
     return SUPABASE_API.revisar_coneccion()

async def api_contactos_crear(form_data: dict):
     return SUPABASE_API.Usuario_ApiInsert(form_data)

async def api_inicio_sesion(form_data: dict):
     return SUPABASE_API.IngresoSesion(form_data)

