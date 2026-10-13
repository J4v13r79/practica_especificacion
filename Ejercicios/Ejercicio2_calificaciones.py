''' 
La calificación final de una materia se obtiene de tres parciales que valen 30%, 30% y 
40%. La materia se aprueba con 70. Un parcial menor a 50 reprueba la materia. Se 
necesita mostrar la calificación final y si el alumno aprobó. 
''' 
# PROBLEMA 
# Qué se calcula, en una oración.
# Se calcula la calificación final de una materia a partir de tres parciales.

# ENTRADAS
# parcial1 : float, 0 < parcial1 < 100
# parcial2 : float, 0 < parcial2 < 100
# parcial3 : float, 0 < parcial3 < 100

# SALIDAS
# calificacion_final : float, 0 < calificacion_final < 100
# aprobado : bool

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 

# ALGORITMO
# 1. Leer parcial1,2,3
# 2. Si parcial1 < 50 o parcial2 < 50 o parcial3 < 50:
#       aprobado = False
# 3. En otro caso:
#       calificacion_final = parcial1 * 0.3 + parcial2 * 0.3 + parcial3 * 0.4
#       aprobado = calificacion_final >= 70
# 4. Mostrar calificacion_final y aprobado

# CASOS DE PRUEBA
# (80, 70, 90) → calificación final: 81; aprobó.
#(70, 70, 70) → calificación final: 70; aprobó.
#(100, 100, 40) → calificación final: 76; reprobó (un parcial es menor a 50).
#(69, 70, 70) → calificación final: 69.7; reprobó.

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leerParciales :leer la calificacion de lso 3 parciales, retorna 3 floats.
# calcularFinal : calcular la calificación final a partir de los parciales, retorna un float.
# determinarEstado : determinar si el alumno aprobó o reprobó, retorna un bool.
# mostrarResultado : mostrar la calificación final y el estado.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerParciales():
    parcial1 = float(input("Ingrese la calificación del primer parcial: "))
    parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
    parcial3 = float(input("Ingrese la calificación del tercer parcial: "))
    return parcial1, parcial2, parcial3

def calcularFinal(parcial1, parcial2, parcial3):
    return parcial1 * 0.3 + parcial2 * 0.3 + parcial3 * 0.4

def determinarEstado(calificacion_final, parcial1, parcial2, parcial3):
    if parcial1 < 50 or parcial2 < 50 or parcial3 < 50:
        return False
    return calificacion_final >= 70

def mostrarResultado(calificacion_final, aprobado):
    print(f"Calificación final: {calificacion_final}")
    if aprobado:
        print("Aprobó.")
    else:
        print("Reprobó.")