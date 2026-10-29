class Calculadora(object):
    def __init__(self):
        self.suma = 0

    def LeerNumeros(self):
        self.numero1 = int(input("Numero 1:"))
        self.numero2 = int(input("Numero 2:"))

    def CalcularSuma(self):
        self.suma = self.numero1 + self.numero2
    
    def MostrarSuma(self):
        print(f"La suma es: {self.suma} ")