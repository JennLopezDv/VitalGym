Ejercicio: Consola de membresía de fitness – Gestión de Miembros y Entrenamientos en Python.
El centro deportivo VitalGym necesita una herramienta en consola desarrollada en Python que permita administrar:

- Miembros | Entrenamientos | Asistencias | Pagos de membresías | Informes mensuales
>>> Toda la persistencia debe manejarse con archivos CSV <<<

>>>>>>>> Inicio de sesión: (Al iniciar, la aplicación solicita usuario y contraseña) <<<<<<<<<

Archivo: usuarios.csv
Campos:
- usuario
- contrasena
- rol
Reglas:
- Validar contra el CSV.
- No se permite registrar nuevos usuarios.
  
Persistencia CSV
3.1 Miembros — miembros.csv
Campos:
- ID de miembro
- nombre
- documento
- teléfono
- correo
- plan (BÁSICO | PREMIUM | COMPLETO)
- fecha_inicio
- fecha_fin_plan
- estado (ACTIVO | INACTIVO)  
3.2 Asistencias —asistencias.csv
Campos:
- asistencia_id
- ID de miembro
- nombre
- fecha
- hora
- tipo (ENTRADA | SALIDA)
3.3 Pagos —pagos.csv
Campos:
- pago_id
- ID de miembro
- nombre
- monto
- fecha_pago
- mes_pagado
- año
- método (EFECTIVO | TARJETA | TRANSFERENCIA)
3.4 Entrenamientos —entrenamientos.csv
Campos:
- entrenamiento_id
- ID de miembro
- fecha
- duración_min
- tipo (CARDIO | FUERZA | HIIT | ESTIRAMIENTO)
- calorías estimadas
  
4. Reglas de negocio
4.1 Estado de membresía
- Solo miembros ACTIVOS pueden entrenar o registrar asistencia.
- Al vencer fecha_fin_plan → estado = INACTIVO.
4.2 Planes y pagos
- Un pago renueva el plan por 30 días.
- No se permiten pagos duplicados del mismo mes y año.
4.3 Cálculo de calorías estimadas
- CARDIO:duracion * 8
- FUERZA:duracion * 5
- Entrenamiento de alta intensidad (HIIT):duracion * 12
- ESTIRAMIENTO:duracion * 3
  
5. Requisitos funcionales
5.1 Gestión de miembros
- Registrador miembro
- Listar miembros (con estado)
- Buscar miembro
- Renovar plan con pago
  
5.2 Asistencias
- Registrar entrada/salida
- Historial por miembro
- 5.3 Entrenamientos
- Entrenamiento de registradores
- Calcular calorías
  
6 Informes CSV
Incluye:
- ID de miembro
- nombre
- asistencias totales
- minutos_entrenados
- calorías_totales
- tipo de entrenamiento
  
7. Requisitos técnicos
Separar en módulos:
- principal.py
- usuarios.py
- miembros.py
- asistencias.py
- entrenamientos.py
- archivos.py
- informes.py
  
8. README.md requerido
Debe incluir:
- Descripción general
- Instrucciones de ejecución
- CSV necesarios
- Reglas de cálculo
- Mejoras futuras
  
9. Diagrama
Diagrama sugerido: flujo de inicio de sesión → menú → registrar actividad.