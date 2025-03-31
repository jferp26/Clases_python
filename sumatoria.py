"""
Realice un programa que reciba como parámetros 2 números enteros.

La función sumará todos los números entre esos dos números, ambos incluidos.

Finalmente imprimirá en pantalla el número obtenido.
"""


def sumatoria(numero1, numero2):
    sumatorio = []
    try:
        if not isinstance(numero1, int) or not isinstance(numero2, int):
            raise TypeError("Deben ser numeros enteros")
        
        if numero1 > numero2:
            for i in range(numero2, numero1 + 1):
                sumatorio.append(i)
        else:
            for i in range(numero1, numero2 + 1):
                sumatorio.append(i)
            
        return sum(sumatorio)
    
    except TypeError as e:
        print(e)
        return None
    except Exception:
        print("Error inesperado")
        return None

def menu():
    while True:
        print("\n1. Calcular suma entre numeros")
        print("2. Salir")
        opcion = input("Elige: ")
        
        if opcion == "1":
            try:
                num1 = int(input("Primer numero: "))
                num2 = int(input("Segundo numero: "))
                resultado = sumatoria(num1, num2)
                if resultado is not None:
                    print("Resultado:", resultado)
            except ValueError:
                print("Solo numeros enteros")
        elif opcion == "2":
            break
        else:
            print("Opcion no valida")

menu()
            
            
        
        
