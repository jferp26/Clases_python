#Ejercicio 1: Calculadora básica con clases
#Crea una clase Calculadora que tenga métodos para sumar, restar, multiplicar y dividir dos números.
#Incluye un constructor que inicialice los dos números como atributos.

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
        try:
            return self.numero1 / self.numero2
        except:
            ZeroDivisionError
            raise("no se puede dividir entre 0")       
    

def menu():
    while True:
        print("CALCULADORA")
        print("1.- SUMA")
        print("2.- RESTA")
        print("3.- MULTIPLICACION")
        print("4.- DIVISION")
        print("5.- SALIR")

        try:
            operacion = int(input("Introduzca la operacion a realizar: "))
        
        except:
            ValueError
            print ("debe introducir un entero del 1 al 5")
            continue
        if operacion == 5:
            print("HASTA LUEGO")
            break
        elif operacion not in [1,2,3,4]:
            print("la operacion no es valida")

        try:
            num1 = int(input("Introduzca el primer numero: "))
            num2 = int(input("Introduzca el segundo numero: "))
        except:
            ValueError
            print("debe introducir numeros")
            continue

        calculeitor = Calculadora(num1, num2)

        if operacion == 1:
            print(f"{num1} + {num2} = {calculeitor.suma()}")
        elif operacion == 2:
            print(f"{num1} - {num2} = {calculeitor.resta()}")
        elif operacion == 3:
            print(f"{num1} x {num2} = {calculeitor.multiplicacion()}")
        elif operacion == 4:
            print(f"{num1} / {num2} = {calculeitor.division()}")
        
     


if __name__ == "__main__":        
  menu()
   
    
    
    
        
        
        
        
