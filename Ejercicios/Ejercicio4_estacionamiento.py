''' 
Un estacionamiento cobra $20 la primera hora y $15 por cada hora adicional o fracción. 
El cobro máximo es de $150. El sistema recibe el tiempo de estancia en minutos y 
muestra el importe a cobrar. 
''' 
# PROBLEMA 
# Qué se calcula, en una oración.
# Se calcula el ticket de estacionamiento a partir del tiempo de estancia.

# ENTRADAS
# tiempo_estancia : int, 0 < tiempo_estancia < ∞

# SALIDAS
# importe_cobrar : float, $, formato: 0.00

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 

# ALGORITMO
# 1. Leer tiempo_estancia en minutos
# 2. Calcular horas_estancia = tiempo_estancia / 60
# 3. Si horas_estancia <= 1:
#       importe_cobrar = 20
# 4. Si 1 < horas_estancia <= 10:
#       importe_cobrar = 20 + (horas_estancia - 1) * 15
# 5. Si horas_estancia > 10:
#       importe_cobrar = 150
# 6. Mostrar importe_cobrar

# CASOS DE PRUEBA
#  45 minutos --  20.00$
#  60 minutos --  20.00$
#  61 minutos --  35.00$
#  150 minutos --  50.00$
#  600 minutos --  150.00$

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leerMinutos: leer el tiempo de estancia en minutos, retorna un int.
# calcularCobro: calcular el importe a cobrar, retorna un float.
# mostrarCobro: mostrar el importe a cobrar en formato 0.00$.

# Implementa el algoritmo anterior utilizando las funciones del contrato.
# asi sea 1 minuto desde la anterior hora se cobra la hora completa
# tener 30 minutos de tolerancia para la primera hora, si se pasa de 30 minutos se cobra la primera hora y desde ahi hasta los 60 minutos se cobra la primera hora y desde ahi se cobra la segunda hora

def leerMinutos():
    tiempo_estancia = int(input("Ingrese el tiempo de estancia en minutos: "))
    return tiempo_estancia

def calcularCobro(tiempo_estancia):
    horas_estancia = tiempo_estancia / 60
    if horas_estancia > 0.5 and horas_estancia <= 1:
        return 20
    elif horas_estancia <= 10:
        return 20 + (horas_estancia - 1) * 15
    else:
        return 150

def mostrarCobro(importe_cobrar):
    print(f"El importe a cobrar es: {importe_cobrar:.2f}$")