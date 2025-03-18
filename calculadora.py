class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def suma(self):
        return self.numero1 + self.numero2

    def resta(self):
        return self.numero1 - self.numero2

    def multiplicacion(self):
        return self.numero1 * self.numero2

    def division(self):
        return self.numero1 / self.numero2

def menu():
    while True:
        print("CALCULADORA")
        print("1.- SUMA")
        print("2.- RESTA")
        print("3.- MULTIPLICACION")
        print("4.- DIVISION")
        print("5.- SALIR")

        operacion = int(input("Introduzca la operacion a realizar: "))
        if operacion == 5:
            print("HASTA LUEGO")
            break

        num1 = int(input("Introduzca el primer numero: "))
        num2 = int(input("Introduzca el segundo numero: "))

        calculator = Calculadora(num1, num2)

        if operacion == 1:
            print(f"{num1} + {num2} = {calculator.suma()}")
        elif operacion == 2:
            print(f"{num1} - {num2} = {calculator.resta()}")
        elif operacion == 3:
            print(f"{num1} x {num2} = {calculator.multiplicacion()}")
        elif operacion == 4:
            print(f"{num1} / {num2} = {calculator.division()}")
if __name__ == "__main__":        
  menu()
   
    
    
    
        
        
        
        
