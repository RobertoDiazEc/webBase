import os
import dotenv
import requests
import time
from supabase import create_client, Client, SupabaseAuthClient, AuthSessionMissingError
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
        response = self.supabase.table("ContactosWeb").select("*").execute()
        #print(response)
        usuarios_data = []
        if len(response.data) > 0:
            for usuarios_item in response.data:
                usuarios_data.append(
                    ItemUsu(nombre = usuarios_item["nombre"], 
                            apellido = usuarios_item["apellido"],
                            email = usuarios_item["email"],
                            celular = usuarios_item["celular"],
                            mensaje = usuarios_item["mensaje"]
                        )
                    )
        return usuarios_data        

    def revisar_coneccion(self) -> str:
        #response = self.supabase.table("WebUsuarios").select("*").execute()
        return "ok enviar datos"
    
    def Usuario_ApiInsert(self, form_data: dict) -> str:
        #response = self.supabase.table("WebUsuarios").select("*").execute()
        querryinsert={"nombre": form_data.get("nombre"),
                    "apellido": form_data.get("apellido"), 
                    "email": form_data.get("email"), 
                    "celular": form_data.get("celular"),
                    "mensaje": form_data.get("mensaje") }
        response = self.supabase.table("ContactosWeb").insert(querryinsert).execute()
        print(response)         
        return " enviado form_data"
            #if response > 200:
                
    def IngresoSesion(self, form_data: dict) -> bool:
        try: 
            usuarioQuerry={
                "email": form_data.get("email"),
                "password": form_data.get("password")
                }
            inwithOAuth={
                "provider": 'google'
            }
            response = self.supabase.auth.sign_in_with_password(usuarioQuerry) 
            print(response)
            if len(response.user.id) > 0:
                return True
        except Exception as e:       
            return False       


   #         signInWithOAuth({
  #             provider: 'google'})
  #sign_in_with_password(usuarioQuerry) 
  #sign_in_with_oauth(inwithOAuth) 
  