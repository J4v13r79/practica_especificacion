

# EJERCICIO 7. Multa
# Cuando superas el limite de velocidad de 60km/h por 1 km/h hasta 20km/h, la multa es de $500.
# Cuando superas el limite de velocidad de 60km/h por mas de 20km/h, la multa es de $1,000. 
# Se necesita mostrar la velocidad del vehiculo y la multa a pagar según la velocidad.

# PROBLEMA 
# Calcular La multa a pagar según la velocidad del vehículo.

# ENTRADAS 
# edad : int, velocidad, valor mayor o igual a 0.

# SALIDAS 
# precio : float, pesos, mostrar con 2 decimales 

# REGLAS Y SUPUESTOS 
# - la multa minima es 500 pesos y la maxima es 1000 pesos. 
# - Consultar la velocidad del vehiculo y la multa a pagar según la velocidad.
# - Si no se excede el limite de velocidad, la multa es de $0.
# - la multa se muestra con 2 decimales. 

# CLASE 
# Nombre: Multa 
# Responsabilidad: almacenar la velocidad del vehículo, calcular la multa a pagar y mostrarla.
# calcular la multa a pagar según la velocidad del vehículo y mostrarla.

# ATRIBUTOS 
# velocidad: int 
#  velocidad de el coche. Valor inicial: 0. 
# multa : float 
#  multa calculado. Valor inicial: 0.0. 

# CONTRATO DE CLASE 
# class multa: 
#__init__(self) -> None: 
#  Inicializa velocidad=0 y multa=0.0.
#leerVelocidad(self) -> None: 
#  Solicita la velocidad y la guarda en self.velocidad.
#calcularMulta(self) -> None: 
#  Calcula la multa según self.velocidad y almacena
#  el resultado en self.multa.
#mostrarMulta(self) -> None:
#  Muestra self.velocidad y self.multa con 2 decimales.


# ALGORITMO 
# 1. Desde menu/menu.py crear un objeto Multa. 
# 2. Ejecutar leervelocidad(). 
# 3. Ejecutar calcularMulta():   
# Si self.velocidad <= 60:
# self.multa = 0    
# En caso contrario, si self.edad >= 60 <= 80: 
# self.multa = 500
#   En caso contrario: 
# self.multa = 1000 
# 4. Ejecutar mostrarMulta(): 
#   mostrar la MULTA a pagar según la velocidad del vehículo.

# CASOS DE PRUEBA 
# 8 años  -> $40.00 
# 12 años -> $40.00 
# 13 años -> $80.00 
# 59 años -> $80.00 
# 60 años -> $40.00 

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

class Multa(object):
    def __init__(self):
        self.velocidad = 0
        self.multa = 0.0

    def leerVelocidad(self):
        self.velocidad = float(input("Ingrese la velocidad del vehículo en km/h: "))

    def calcularMulta(self):
        if self.velocidad <= 60:
            self.multa = 0
        elif self.velocidad <= 80:
            self.multa = 500
        else:
            self.multa = 1000

    def mostrarMulta(self):
        print(f"Velocidad del vehículo: {self.velocidad:.2f} km/h")
        print(f"Multa a pagar: ${self.multa:.2f}")