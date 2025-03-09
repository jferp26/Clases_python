import random

class Cuenta:
    cuentas_creadas=[]
    def __init__(self,saldo_inicial):
        self.numero = random.randint(1000000000000000000,99999999999999999)
        self.saldo = saldo_inicial
        self.riesgo = 1
        while True:
             self.numero = random.randint(1000000000000000000,99999999999999999)
             if self.numero not in Cuenta.cuentas_creadas:
                 self.saldo=saldo_inicial
                 self.riesgo = 1
                 Cuenta.cuentas_creadas.append(self.numero)
    
    def setnumero(self,num):
        self.numero=num

    def getnumero(self):
        return self.numero
    
    def getsaldo(self):
        return self.saldo
    
    def ingresar(self,cantidad):
        self.saldo +=cantidad
    
    def retirada(self,cantidad):
        self.saldo -= cantidad
    
cuenta1 = Cuenta(1000,)
cuenta2 = Cuenta()
print(Cuenta.cuentas_creadas)