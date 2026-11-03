# EJERCICIO 6. BOLETO DE CINE 
# Un cine cobra $80 por boleto. 
# Los niños de hasta 12 años y los adultos de 60 años 
# o más pagan la mitad. 
# Se necesita mostrar el precio según la edad. 

# PROBLEMA 
# Calcular el precio de un boleto según la edad. 

# ENTRADAS 
# edad : int, años, valor mayor o igual a 0. 
# SALIDAS 
# precio : float, pesos, mostrar con 2 decimales

# REGLAS Y SUPUESTOS 
# - El precio normal es de $80. 
# - Los niños de 12 años o menos pagan $40. 
# - Los adultos de 60 años o más pagan $40. 
# - Las personas de 13 a 59 años pagan $80. 
# - Con 12 años paga $40; con 60 años paga $40. 
# - Las edades se expresan en años completos. 
# - Se supone que la edad ingresada es válida. 
# - El precio se muestra con 2 decimales. 

# CLASE 
# Nombre: BoletoCine 
# Responsabilidad: almacenar la edad de una persona, 
# calcular el precio de su boleto y mostrarlo. 

# ATRIBUTOS 
# edad : int 
#   Edad de la persona. Valor inicial: 0. 
# precio : float 
#  Precio calculado. Valor inicial: 0.0. 

# CONTRATO DE CLASE 
# class BoletoCine: 
#__init__(self) -> None: 
#  Inicializa edad=0 y precio=0.0. 
#leerEdad(self) -> None: 
#  Solicita la edad y la guarda en self.edad. 
#calcularPrecio(self) -> None: 
#  Calcula el precio según self.edad y almacena 
#  el resultado en self.precio. 
#mostrarPrecio(self) -> None: 
# Muestra self.edad y self.precio con 2 decimales. 

# ALGORITMO 
# 1. Desde menu/menu.py crear un objeto BoletoCine. 
# 2. Ejecutar leerEdad(). 
# 3. Ejecutar calcularPrecio(): 
#   Si self.edad <= 12: 
#self.precio = 80 * 0.50 
#En caso contrario, si self.edad >= 60: 
#self.precio = 80 * 0.50 
#Programación Aplicada   
#Ing. Alejandro Montes        
#En caso contrario: 
#self.precio = 80 
# 4. Ejecutar mostrarPrecio(): 
#  mostrar la edad y el precio con 2 decimales. 
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

class BoletoCine(object):
    def __init__(self):
        self.edad = 0
        self.precio = 0.0

    def leerEdad(self):
        self.edad = int(input("Ingrese la edad del espectador: "))

    def calcularPrecio(self):
        if self.edad <= 12:
            self.precio = 80 * 0.50
        elif self.edad >= 60:
            self.precio = 80 * 0.50
        else:
            self.precio = 80

    def mostrarPrecio(self):
        print(f"Edad: {self.edad} años, Precio del boleto: ${self.precio:.2f}")