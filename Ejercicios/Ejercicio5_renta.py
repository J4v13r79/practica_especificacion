''' 
Un parque renta bicicletas a $30 por hora. Si se rentan 3 horas o más, se aplica un 15% de descuento. Se 
necesita mostrar el importe a pagar según las horas de renta. 
''' 
# PROBLEMA 
# Qué se calcula, en una oración.
# Se calcula el importe a pagar por la renta de bicicletas según las horas de uso.

# ENTRADAS
# horas_renta : float, horas, 0 < horas_renta < ∞

# SALIDAS
# importe_recibo : float, $, formato: 0.00

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 

# ALGORITMO
# 1. Leer horas_renta
# 2. Si horas_renta < 3:
#       importe_recibo = horas_renta * 30
# 3. En otro caso:
#       importe_recibo = horas_renta * 30 * 0.85
# 4. Mostrar importe_recibo 

# CASOS DE PRUEBA
# 1h -- 30.00$
# 2h -- 60.00$
# 3h -- 76.50$
# 4h -- 102.00$

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leerHoras: leer las horas de renta, retorna un float.
# calcularRenta: calcular el importe a pagar por la renta de bicicletas, retorna un float.
# mostrarRenta: mostrar el importe a pagar por la renta de bicicletas.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerHoras():
    horas_renta = float(input("Ingrese las horas de renta: "))
    return horas_renta

def calcularRenta(horas_renta):
    if horas_renta < 3:
        return horas_renta * 30
    else:
        return horas_renta * 30 * 0.85

def mostrarRenta(importe_recibo):
    print(f"El importe a pagar por la renta de bicicletas es: {importe_recibo:.2f}$")