import reflex as rx

    
class ItemUsu(rx.Base):
    """para enviar contactos a supabase"""
    nombre: str
    apellido: str 
    email: str
    celular: str
    mensaje: str
   

class UserRegistrado(rx.Base):
    """para que este regisrado en supabase"""
    username: str
    password: str   