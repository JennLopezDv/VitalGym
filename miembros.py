import os
from utilidades import *
from datetime import datetime, timedelta

RUTA_MIEMBROS = os.path.join("datos", "miembros.csv")

def validar_miembros(documento):
    miembros = leer_datos(RUTA_MIEMBROS)

    for m in miembros:
        if m["documento"] == documento
        return True
