

# EJERCICIO 5. Renta de bicicletas
# se renta una bicicleta a $30 por hora. Si se rentan 3 horas o más, se aplica un 15% de descuento. 
# se debe msotrar el importe a pagar según las horas de renta.

# PROBLEMA 
# Calcular el importe a pagar por la renta de bicicletas según las horas de uso.

# ENTRADAS 
# tiempo : int, horas, valor mayor o igual a 0. 
# SALIDAS 
# Importe : float, pesos, mostrar con 2 decimales

# REGLAS Y SUPUESTOS 
# - Una hora son 30$.
# - cuando se rentan 3 horas o más, se aplica un 15% de descuento. 
# - El tiempo se expresa en horas completas. 
# - El importe se muestra con 2 decimales. 

# CLASE 
# Nombre: RentaBici
# Responsabilidad: almacenar el tiempo de renta de bicicletas
#  calcular el importe a pagar y mostrarlo.


# ATRIBUTOS 
# tiempo : int 
#   tiempo de renta. Valor inicial: 0. 
# importe : float 
#  importe calculado. Valor inicial: 0.0. 

# CONTRATO DE CLASE 
# class RentaBici: 
#__init__(self) -> None: 
#  Inicializa tiempo=0 y importe=0.0.
#leerTiempo(self) -> None: 
#  Solicita el tiempo y lo guarda en self.tiempo.
#calcularImporte(self) -> None: 
#  Calcula el importe según self.tiempo y almacena

# ALGORITMO 
# 1. Desde menu/menu.py crear un objeto BoletoCine. 
# 2. Ejecutar leerRentaBici(). 
# 3. Ejecutar calcularRentaBici(): 
#   Si self.tiempo < 3:
#  return self.tiempo * 30
#En caso contrario, si self.tiempo >=3: 
#self.Importe = self.tiempo * 30 * 0.85     
# 4. Ejecutar mostrarRentaBici(): 
#  mostrar el importe y el precio con 2 decimales. 

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente la clase BoletoCine. 
# - Usa los atributos y métodos del contrato. 
# - Inicializa los atributos en __init__. 
# - Utiliza self para acceder a los atributos. 
# - Conserva las reglas y el orden del algoritmo. 
# - No agregues funciones auxiliares ni otras clases. 
# - No agregues validaciones, mensajes ni cálculos 
#   no especificados. 
# - No crees ni uses objetos en este archivo; 
#   se crean y ejecutan desde menu/menu.py. 
# - No agregues bibliotecas innecesarias. 

# Implementa la clase según esta especificación. 

class RentaBici(object):
    def __init__(self):
        self.horas_renta = 0
        self.importe_recibo = 0

    def LeerHoras(self):
        self.horas_renta = float(input("Ingrese las horas de renta: "))

    def CalcularRenta(self):
        PRECIO_HORA = 30.00
        DESCUENTO = 0.15

        self.importe_recibo = self.horas_renta * PRECIO_HORA

        if self.horas_renta >= 3:
            self.importe_recibo = self.importe_recibo * (1 - DESCUENTO)

    def MostrarRenta(self):
        print(f"Horas de renta: {self.horas_renta}")
        print(f"Importe a pagar: ${self.importe_recibo:.2f}")