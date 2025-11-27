import csv
import unicodedata
import re

#Funciones leer y guardar archivos CSV:

def leer_datos(ruta):       
    try:
        with open(ruta, newline= '', encoding='utf-8') as archivo:
            return list(csv.DictReader(archivo))
            
    except FileNotFoundError:
        print(f"¡Error! Archivo no encontrado: {ruta}")
        return []


def guardar_datos(ruta, datos):    
    if len(datos) == 0:
        raise ValueError("No hay datos para agregar")

    # Leer contenido existente usando leer_csv
    datos_existentes = leer_datos(ruta)
    archivo_vacio = len(datos_existentes) == 0

    # Determinar encabezados
    if not archivo_vacio:
        encabezados = list(datos_existentes[0].keys())
    else:
        encabezados = list(datos[0].keys())

    # Abrir el archivo en modo 'a' para agregar al final
    with open(ruta, 'a', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)

        # Escribir encabezado solo si el archivo estaba vacío
        if archivo_vacio:
            escritor.writeheader()

        # Escribir las filas nuevas
        escritor.writerows(datos)


#Funciones para números enteros y flotantes:

def validar_entero_positivo(valor):
    if not valor.isdigit():
        raise ValueError("Error: El valor debe ser un entero positivo.")
    valor = int(valor)
    if valor <= 0:
        raise ValueError("Error: El valor debe ser mayor a cero.")
    return valor

def validar_positivo_float(valor):
    try:
        valor = float(valor)
    except ValueError:
        raise ValueError("Error: El valor debe ser un número positivo.")
    if valor <= 0:
        raise ValueError("Error: El valor debe ser mayor a cero.")
    return valor

#Función para limpiar Strings:
def limpiar_string(texto):    
    texto_norm = unicodedata.normalize('NFKD', texto)
    
    texto_sin_tildes = "".join(
        c for c in texto_norm
        if not unicodedata.combining(c)
    )    
    texto_limpio = re.sub(r"[^a-zA-Z0-9\s]", "", texto_sin_tildes)
    return texto_limpio