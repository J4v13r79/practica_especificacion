from Clases.Ejemplo.Calculadora import Calculadora
 
 
class Menu(object):
    def __init__(self):
        self.opcion = 0



def mostrar_Menu(self):
    print()
    print("Ejemplo programacion orientado a objetos") 
    print("1. Calculadora") 
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
        else:
            print("Opción no válida.")