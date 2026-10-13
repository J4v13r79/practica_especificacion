''' 
Una tienda aplica 10% de descuento en compras de $1,000 o más y 20% en compras de 
$5,000 o más. A la compra se le agrega el 16% de IVA. Se necesita mostrar el ticket con 
subtotal, descuento, IVA y total. 
''' 
# PROBLEMA 
# Qué se calcula, en una oración.
# Se calcula el ticket de compra a partir del precio.

# ENTRADAS
# Precio : float, 0 < Precio < 100000

# SALIDAS
# subtotal : float, 0 < subtotal < 100000
# descuento : float, 0 < descuento < 100000
# IVA : float, 0 < IVA < 100000
# total : float, 0 < total < 100000

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 

# ALGORITMO
# 1. Leer Precio de la compra
# 2. Si Precio < 1000:
#       descuento = 0
# 3. Si 1000 <= Precio < 5000:
#       descuento = Precio * 0.1
# 4. Si Precio >= 5000:
#       descuento = Precio * 0.2
# 5. subtotal = Precio - descuento
# 6. IVA = subtotal * 0.16
# 7. total = subtotal + IVA
# 4. Mostrar calificacion_final y aprobado

# CASOS DE PRUEBA
#$500 → subtotal: $500.00; descuento: $0.00; IVA: $80.00; total: $580.00
#$900 → subtotal: $900.00; descuento: $0.00; IVA: $144.00; total: $1,044.00
#$1,000 → subtotal: $1,000.00; descuento: $100.00; IVA: $144.00; total: $1,044.00
#$5,000 → subtotal: $5,000.00; descuento: $1,000.00; IVA: $640.00; total: $4,640.00

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leerSubtotal : leer el subtotal de la compra, retorna un float.
# calcularDescuento : calcular el descuento a aplicar, retorna un float.
# calcularIVA : calcular el IVA a agregar, retorna un float.
# calcularTotal : calcular el total a pagar, retorna un float.
# mostrarTicket : mostrar el ticket de compra.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerSubtotal():
    subtotal = float(input("Ingrese el subtotal de la compra: "))
    return subtotal

def calcularDescuento(subtotal):
    if subtotal < 1000:
        return 0
    elif subtotal < 5000:
        return subtotal * 0.1
    else:
        return subtotal * 0.2

def calcularIVA(subtotal):
    return subtotal * 0.16

def calcularTotal(subtotal, descuento, iva):
    return subtotal - descuento + iva

def mostrarTicket(subtotal, descuento, iva, total):
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"Total: ${total:.2f}")