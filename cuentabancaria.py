class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser positiva.")
        self.saldo += cantidad
        print(f"Se han depositado {cantidad} euros. Saldo actual: {self.saldo} euros.")

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.saldo:
            raise ValueError("No puede retirar más de lo que hay en la cuenta.")
        self.saldo -= cantidad
        print(f"Se han retirado {cantidad} euros. Saldo actual: {self.saldo} euros.")

    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo:} euros.")

def menu():
    cuenta = None
    while True:
        print("### BIENVENIDO A EVO BANCO ###")
        print("1. Crear nueva cuenta bancaria")
        print("2. Operar con su cuenta bancaria")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            titular = input("Introduzca el nombre del titular de la cuenta: ")
            cuenta = CuentaBancaria(titular)
            print(f"Cuenta de {titular} creada con éxito.")
        elif opcion == 2:
            if cuenta is None:
                print("Primero debe crear una cuenta bancaria (opción 1).")
                continue
            while True:
                print("\n¿Qué operación desea realizar?")
                print("1. Ingresar dinero")
                print("2. Retirar dinero")
                print("3. Consultar saldo")
                print("4. Volver al menú principal")
                operacion = int(input("Seleccione una operación: "))
                
                if operacion == 1:
                    try:
                        cantidad = float(input("Introduzca el importe a ingresar: "))
                        cuenta.depositar(cantidad)
                    except ValueError as e:
                        print(e)
                elif operacion == 2:
                    try:
                        cantidad = float(input("Introduzca el importe a retirar: "))
                        cuenta.retirar(cantidad)
                    except ValueError as e:
                        print(e)
                elif operacion == 3:
                    cuenta.consultar_saldo()
                elif operacion == 4:
                    break
                else:
                    print("Opción no válida.")
        elif opcion == 3:
            print("Salir del programa. ¡Hasta luego!")
            break
        else:
            print("Opcion no valida.")

menu()
