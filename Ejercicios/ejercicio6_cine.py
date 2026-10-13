''' 
Un cine cobra $80 por boleto. Los niños de hasta 12 años y los adultos de 60 años o más pagan la mitad. 
Se necesita mostrar el precio del boleto según la edad. 
''' 
# PROBLEMA 
# Qué se calcula, en una oración.
# Se calcula el precio del boleto de cine según la edad del espectador.

# ENTRADAS
# edad : int, años, 0 < edad < ∞

# SALIDAS
# importe_recibo : float, $, formato: 0.00

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 

# ALGORITMO
# 1. Leer edad
# 2. Si edad <= 12 o edad >= 60:
#       importe_recibo = 80 * 0.5
# 3. En otro caso:
#       importe_recibo = 80
# 4. Mostrar importe_recibo

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leerEdad: leer la edad del espectador, retorna un int.
# calcularPrecio: calcular el precio del boleto según la edad, retorna un float.
# mostrarPrecio: mostrar el precio del boleto según la edad.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerEdad():
    edad = int(input("Ingrese la edad del espectador: "))
    return edad

def calcularPrecio(edad):
    if edad <= 12 or edad >= 60:
        return 80 * 0.5
    else:
        return 80

def mostrarPrecio(importe_recibo):
    print(f"El precio del boleto de cine es: {importe_recibo:.2f}$")