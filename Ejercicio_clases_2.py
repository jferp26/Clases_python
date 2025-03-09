# crea la clase "Cuenta". Cada cuenta tendrá un número (diferente a las demás) y un saldo (float)
# El número de cuenta se puede consultar y modificar (getter y setter) pero el saldo sólo puede consultarse (getter).
# Para modificar el saldo tenemos que hacer un ingreso o una retirada.

class Cuenta:
    saldocuenta=0
    def __init__(self,ncuenta):
        self.ncuenta=ncuenta
        

    def set_ncuenta(self, ncuenta):
        self.ncuenta = ncuenta

    def get_ncuenta(self):
        return self.ncuenta
    
    def get_saldocuenta(self):
        return self.saldocuenta
    
    def ingresardinero(self):
        saldocuenta = float(input("Introduzca el importe que quiere ingresar en la cuenta: "))
        self.saldocuenta = saldocuenta

    def retirardinero(self):
        saldo_actual = float(input("Introduzca el importe que quiere retirar de la cuenta: "))
        self.saldocuenta = saldo_actual

    def ingresar(self, cantidad):
        self.saldocuenta += cantidad
  
    def retirar(self, cantidad):
        self.saldocuenta-=cantidad
       


cuenta1 = Cuenta(123456789)
print(f"Número de cuenta: {cuenta1.ncuenta}")
print(f"Saldo inicial: {cuenta1.saldocuenta}")

cuenta1.ingresar(2000)
print(f"Saldo después del ingreso: {cuenta1.saldocuenta}")

cuenta1.retirar(500)
print(f"Saldo después de la retirada: {cuenta1.saldocuenta}")
