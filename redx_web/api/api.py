
from .Supabase_api import Supabase_API
from ..model.userweb import ItemUsu

SUPABASE_API = Supabase_API()

async def api_usuarios() -> list[ItemUsu]:
    return SUPABASE_API.Usuario_ApiBase()

