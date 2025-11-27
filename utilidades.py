import csv

#Funciones leer y guardar archivos CSV:

def leer_datos(ruta):       
    try:
        with open(ruta, newline= '', encoding='utf-8') as archivo:
            return list(csv.DictReader(archivo))
            
    except FileNotFoundError:
        print(f"¡Error! Archivo no encontrado: {ruta}")
        return []


def guardar_datos(ruta, datos, nombrecarpeta):    
    with open(ruta, "w", newline= '', encoding='utf-8') as archivo:
        write = csv.DictWriter(archivo, nombrecarpeta=nombrecarpeta)
        write.writeheader()
        write.writerows(datos)


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

      