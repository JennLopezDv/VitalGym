import os
from utilidades import *
from datetime import datetime, timedelta

RUTA_MIEMBROS = os.path.join("datos", "miembros.csv")
miembros = leer_datos(RUTA_MIEMBROS)

def registrar_miembro():
    print(">>> Agregar miembro <<<")
    if miembros:
        id_miembro = max(int(m["id_miembro"]) for m in miembros)
    else:
        id_miembro = 0

    while True:
        nombre = input("Ingrese nombre: ").strip() #.strip() elimina espacios en blanco, saltos de línea, tabulacione, al inicio y al final de un string
        if nombre != "":
            break
        print("Ingrese nombre válido.")
    
    while True:
        documento = input("Ingrese número de documento: ")
        try:
            validar_entero_positivo(documento)
            break
        except ValueError:
            print("Debe ingresar únicamente números positivos.")

    while True:
        telefono = input("Ingrese teléfono: ")
        try:
            validar_entero_positivo(telefono)
            break
        except ValueError:
            print("Debe ingresar únicamente números positivos.")

    while True:
        correo = input("Ingrese correo: ").strip()
        if correo != "":
            break
        print("Ingrese correo válido.")
    
    opcion_plan = ("BASICO", "PREMIUM", "COMPLETO")
    while True:
        tipo_plan = input("Eliga tipo de plan: Básico | Premium | Completo: ").strip().upper()
        opcion_valida = limpiar_string(tipo_plan).upper().strip()
        if opcion_valida in opcion_plan:
            break
        print("¡Opción no válida! Eliga nuevamente: ")

    fecha_inicio = datetime.now().strftime("%Y-%m-%d")
    fecha_fin_plan = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")    

    opciones_estado = ("ACTIVO", "INACTIVO")
    while True:
        estado = input("Ingrese estado (Activo / Inactivo): ").strip().upper()
        if estado in opciones_estado:
            break
        print("¡Estado inválido! Debe ser ACTIVO o INACTIVO.")

    miembro = {
        "id" : id_miembro +1,
        "nombre" : nombre,
        "documento" : documento,
        "telefono" : telefono,
        "correo" : correo,
        "tipo_plan" : tipo_plan,
        "fecha_inicio" : fecha_inicio,
        "fecha_fin" : fecha_fin_plan,
        "estado" : estado
    }

    guardar_datos(RUTA_MIEMBROS, [miembro])

    
registrar_miembro()






