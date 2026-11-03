from Clases.Ejemplo.Calculadora import Calculadora
from Clases.Ejemplo.Ejercicios.Recibo import Recibo
from Clases.Ejemplo.Ejercicios.Calificaciones import Calificaciones
from Clases.Ejemplo.Ejercicios.BoletoCine import BoletoCine
from Clases.Ejemplo.Ejercicios.Multa import Multa


class Menu(object):
    def __init__(self):
        self.opcion = " "

    def mostrar_Menu(self):
        print()
        print("Ejemplo programacion orientado a objetos")
        print("1. Calculadora")
        print("2. Recibo de electricidad")
        print("3. Calificaciones")
        print("4. Boleto de cine")
        print("5. Multa")
        print("0. Salir")

    def menus(self):
        self.opcion = ""

        while self.opcion != "0":
            self.mostrar_Menu()
            self.opcion = input("Seleccione una opción: ")

            if self.opcion == "1":
                casio = Calculadora()
                casio.LeerNumeros()
                casio.CalcularSuma()
                casio.MostrarSuma()

            elif self.opcion == "2":
                recibo = Recibo()
                recibo.LeerConsumo()
                recibo.CalcularPago()
                recibo.MostrarRecibo()

            elif self.opcion == "3":
                alumno = Calificaciones()
                alumno.LeerParciales()
                alumno.CalcularFinal()
                alumno.DeterminarEstado()
                alumno.MostrarResultado()
            
            elif self.opcion == "4":
                boleto = BoletoCine()
                boleto.leerEdad()
                boleto.calcularPrecio()
                boleto.mostrarPrecio()
            
            elif self.opcion == "5":
                multa = Multa()
                multa.leerVelocidad()
                multa.calcularMulta()
                multa.mostrarMulta()

            elif self.opcion == "0":
                print("Saliendo del programa...")

            else:
                print("Opción no válida.")