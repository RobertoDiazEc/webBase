from enum import Enum

class Route(Enum):
    INDEX = "/"
    CONTACTOS = "/contactos"
    PRODUCTOS = "/productos"
    COMUNIDAD = "/comunidad"
    REGISTRATE = "/protected"
    


class RouteImagen(Enum):
    BIENVENIDO = "/imagenes/bienvenidos2.jpg"
    SOMOSREDX = "/imagenes/programacion.png"
    PORTADA = "/imagenes/portadaRedx1.jpg"
    COMUNIDAD = "/comunidad"
    CONTACTOS = "/contactos"
    MENUINTENO = "/menuinterno"