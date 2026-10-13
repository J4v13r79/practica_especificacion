from Ejercicios.Ejercicios1_luz import leerConsumo, calcularPago, mostrarRecibo
from Ejercicios.Ejercicio2_calificaciones import leerParciales, calcularCalificacionFinal,determinarEstado, mostrarResultado
from Ejercicios.Ejercicio3_compra import leerSubtotal, calcularDescuento, calcularIVA, calcularTotal, mostrarTicket
from Ejercicios.Ejercicio4_estacionamiento import leerMinutos, calcularCobro, mostrarCobro  
 
 
def ejecutarEjercicio1(): 
    consumo_kwh = leerConsumo() 
    importe_recibo = calcularPago(consumo_kwh) 
    mostrarRecibo(consumo_kwh, importe_recibo)


def ejecutarEjercicio2():
    parcial1, parcial2, parcial3 = leerParciales()
    calificacion_final = calcularCalificacionFinal(parcial1, parcial2, parcial3)
    aprobado = determinarEstado(calificacion_final, parcial1, parcial2, parcial3)
    mostrarResultado(calificacion_final, aprobado)


def ejecutarEjercicio3():
    subtotal = leerSubtotal()
    descuento = calcularDescuento(subtotal)
    iva = calcularIVA(subtotal)
    total = calcularTotal(subtotal, descuento, iva)
    mostrarTicket(subtotal, descuento, iva, total)


def ejecutarEjercicio4():
    tiempo_estancia = leerMinutos()
    importe_cobrar = calcularCobro(tiempo_estancia)
    mostrarCobro(importe_cobrar)


def mostrarMenu():
    print()
    print("PRÁCTICA: DESARROLLO GUIADO POR ESPECIFICACIÓN") 
    print("1. Recibo de luz") 
    print("2. Calificación final") 
    print("3. Total de compra") 
    print("4. Estacionamiento") 
    print("0. Salir") 
 
 
def menus(): 
    opcion = "" 
    while opcion != "0": 
        mostrarMenu() 
        opcion = input("Seleccione una opción: ") 
        if opcion == "1": 
            ejecutarEjercicio1() 
        elif opcion == "2": 
            ejecutarEjercicio2() 
        elif opcion == "3": 
            ejecutarEjercicio3() 
        elif opcion == "4": 
            ejecutarEjercicio4() 
        elif opcion != "0": 
            print("Opción no válida.")