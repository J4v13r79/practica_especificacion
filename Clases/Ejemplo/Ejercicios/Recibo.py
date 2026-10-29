class Recibo(object):
    def __init__(self):
        self.consumo_kwh = 0
        self.importe_recibo = 0

    def LeerConsumo(self):
        self.consumo_kwh = float(input("Ingrese el consumo del mes en kWh: "))

    def CalcularPago(self):
        if self.consumo_kwh <= 150:
            self.importe_recibo = self.consumo_kwh * 1.00
        elif self.consumo_kwh <= 280:
            self.importe_recibo = 150 * 1.00 + (self.consumo_kwh - 150) * 1.50
        else:
            self.importe_recibo = 150 * 1.00 + (280 - 150) * 1.50 + (self.consumo_kwh - 280) * 3.00

    def MostrarRecibo(self):
        print(f"Consumo: {self.consumo_kwh} kWh")
        print(f"Importe: ${self.importe_recibo:.2f}")