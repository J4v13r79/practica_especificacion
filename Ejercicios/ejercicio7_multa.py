''' 
En una avenida el límite es de 60 km/h. Si se excede hasta por 20 km/h, la multa es de $500. Si se excede 
por más de 20 km/h, la multa es de $1,000. Se necesita mostrar la multa a partir de la velocidad del 
vehículo. 
''' 
# PROBLEMA 
# Qué se calcula, en una oración.
# Se calcula la multa a pagar según la velocidad del vehículo.

# ENTRADAS
# velocidad : float, km/h, 0 < velocidad < ∞

# SALIDAS
# importe_recibo : float, $, formato: 0.00

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 

# ALGORITMO
# 1. Leer velocidad
# 2. Si velocidad <= 60:
#       importe_recibo = 0
# 3. Si velocidad > 60 y velocidad <= 80:
#       importe_recibo = 500
# 4. Si velocidad > 80:
#       importe_recibo = 1000
# 5. Mostrar importe_recibo

# CASOS DE PRUEBA
# 50, 60, 61, 80 y 81 km/h 

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leerVelocidad: leer la velocidad del vehículo, retorna un float.
# calcularMulta: calcular la multa a pagar según la velocidad, retorna un float.
# mostrarMulta: mostrar la multa a pagar según la velocidad.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerVelocidad():
    velocidad = float(input("Ingrese la velocidad del vehículo en km/h: "))
    return velocidad

def calcularMulta(velocidad):
    if velocidad <= 60:
        return 0
    elif velocidad <= 80:
        return 500
    else:
        return 1000

def mostrarMulta(importe_recibo):
    print(f"La multa a pagar es: {importe_recibo:.2f}$")