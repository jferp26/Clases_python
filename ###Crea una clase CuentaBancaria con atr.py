###Crea una clase CuentaBancaria con atributos para titular y saldo.
###Añade métodos para depositar, retirar y consultar el saldo. Usa el manejo de excepciones para evitar 
###saldos negativos.

class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
    
    def ingresar(self):
        ingreso = float(input(" Introduzca el importe a ingresar con un punto y 2 decimales: "))
        self.saldo += ingreso
        return self.saldo
    
    def retirar(self):
        try:
            ingreso = int(input(" Introduzca el importe a retirar: "))
            self.saldo += ingreso
            return self.saldo
        
        except Exception: self.saldo <0
        raise "el saldo no puede ser negativo"

    def mostrarsaldo(self):
        return self.saldo

def menu():
    cuenta = "vacia"
    while True:
        print("### BIENVENIDO A EVO BANCO ###")
        print("¿QUE OPERACION DESEA REALIZAR?")
        print("1. crear nueva cuenta bancaria")
        print("2. Operar con su cuenta bancaria")
        print("3. Salir")
        try:
            opcion = int(input("Selecciona una opción: "))
            opcionesvalidas=[1,2,3]
        except:
            if opcion not in opcionesvalidas:
                raise "operacion no valida, debe seleccionar una opcion del menu:"
            continue

        if opcion == 1:
            titular = input("introduzca el nombre del titular de la cuenta")
            saldo = 0
            cuenta = CuentaBancaria(titular,saldo)
            print(f"la cuenta de {titular} se ha creado con exito")
            print("si desea operar con su cuenta seleccione la opcion 2 del menu principal de lo contrario opcion 3 salir")
            continue
        
        elif opcion == 2:
                while True:
                    print("¿QUE OPERACION DESEA REALIZAR?")
                    print("1. ingresar dinero")
                    print("2. retirar dinero")
                    print("3. consultar el saldo")
                    
            try:
            opcion = int(input("Selecciona una opción: "))
            opcionesvalidas=[1,2,3]
        except:
            if opcion not in opcionesvalidas:
                raise "operacion no valida, debe seleccionar una opcion del menu:"
            continue
            saldo = 0
            cuenta = CuentaBancaria(titular,saldo)
            print(f"la cuenta de {titular} se ha creado con exito")
            print("si desea operar con su cuenta seleccione la opcion 2 del menu principal")
            continue

        elif opcion == 3:
            print("Salir del programa. ¡Hasta luego!")
            break

menu()


    
     

    

        
