''' 
Una compañía eléctrica cobra el consumo mensual con tres tarifas: $1.00 por kWh hasta 
150 kWh, $1.50 por kWh de 151 a 280 kWh y $3.00 por kWh arriba de 280 kWh. Se 
necesita calcular el importe del recibo a partir del consumo del mes. 
''' 
# PROBLEMA 
# Qué se calcula, en una oración.
# Se calcula el importe del recibo de luz a partir del consumo mensual en kWh.

# ENTRADAS
# consumo_kwh : float, kWh, 0 < consumo_kwh < ∞

# SALIDAS
# importe_recibo : float, $, formato: 0.00

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 

# ALGORITMO
# 1. Leer consumo_kwh
# 2. Si consumo_kwh <= 150: 
#       importe_recibo = consumo_kwh * 1.00
# 3. En otro caso: 
#       importe_recibo = 150 * 1.00 + (consumo_kwh - 150) * 1.50
# 4. Si consumo_kwh > 280:
#       importe_recibo = 150 * 1.00 + (280 - 150) * 1.50 + (consumo_kwh - 280) * 3.00
# 5. Mostrar importe_recibo

# CASOS DE PRUEBA
# 100kWh--< 100$
# 150kWh--< 150$
# 200kWh--< 225$
# 280kWh--< 345$
# 300kWh -> 405$

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leerConsumo: leer el consumo del mes en kWh, retorna un float.
# calcularPago: calcular el importe del recibo a partir del consumo en kWh, retorna un float.
# mostrarRecibo: mostrar el recibo con el consumo y el importe.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerConsumo():
    consumo_kwh = float(input("Ingrese el consumo del mes en kWh: "))
    return consumo_kwh

def calcularPago(consumo_kwh):
    if consumo_kwh <= 150:
        return consumo_kwh * 1.00
    elif consumo_kwh <= 280:
        return 150 * 1.00 + (consumo_kwh - 150) * 1.50
    else:
        return 150 * 1.00 + (280 - 150) * 1.50 + (consumo_kwh - 280) * 3.00

def mostrarRecibo(consumo_kwh, importe_recibo):
    print(f"Consumo: {consumo_kwh} kWh")
    print(f"Importe: ${importe_recibo:.2f}")