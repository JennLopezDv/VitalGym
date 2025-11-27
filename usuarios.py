import os
from utilidades import *

RUTA_USUARIOS = os.path.join("datos", "usuarios.csv")

def validar_usuario(usuario, contraseña):
    usuarios = leer_datos(RUTA_USUARIOS)

    for u in usuarios:
        if u["usuario"] == usuario and u["contraseña"] == contraseña:
            return True, u["rol"]
        
    return False, None
    

