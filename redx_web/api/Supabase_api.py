import os
import dotenv
import requests
import time
from supabase import create_client, Client
from ..model.userweb import ItemUsu


class Supabase_API:
        
    dotenv.load_dotenv()
    SUPABASE_URL: str = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY: str = os.environ.get("SUPABASE_KEY")
    
   
       #response = supabase.table("countries").select("*").execute()
    def __init__(self) -> None:
          if self.SUPABASE_URL!= None and self.SUPABASE_KEY != None:
              self.supabase: Client = create_client(self.SUPABASE_URL, self.SUPABASE_KEY)

    def Usuario_ApiBase(self) -> list[ItemUsu]:

            response = self.supabase.table("WebUsuarios").select("*").execute()
            usuarios_data = []
            if len(response.data) > 0:
                for usuarios_item in response.data:
                    usuarios_data.append(
                         ItemUsu(nombre=usuarios_item["nombre"], 
                                 email=usuarios_item["email"]
                                 )
                              )
            
            return usuarios_data        
