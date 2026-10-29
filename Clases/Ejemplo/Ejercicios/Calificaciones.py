class Calificaciones(object):
    def __init__(self):
        self.parcial1 = 0
        self.parcial2 = 0
        self.parcial3 = 0
        self.calificacion_final = 0
        self.aprobado = False

    def LeerParciales(self):
        self.parcial1 = float(input("Ingrese la calificación del primer parcial: "))
        self.parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
        self.parcial3 = float(input("Ingrese la calificación del tercer parcial: "))

    def CalcularFinal(self):
        self.calificacion_final = self.parcial1 * 0.3 + self.parcial2 * 0.3 + self.parcial3 * 0.4

    def DeterminarEstado(self):
        if self.parcial1 < 7 or self.parcial2 < 7 or self.parcial3 < 7:
            self.aprobado = False
        else:
            self.aprobado = self.calificacion_final >= 7

    def MostrarResultado(self):
        print(f"Calificación final: {self.calificacion_final:.2f}")
        if self.aprobado:
            print("Aprobó.")
        else:
            print("Reprobó.")