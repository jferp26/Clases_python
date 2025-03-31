""""""
"""Ejercicio 13: Rectángulo
Crea una clase Rectangulo con atributos para ancho y alto.
Incluye métodos para calcular el área y el perímetro, usando un constructor para inicializar los valores."""

class Rectangulo:
    def __init__(self, ancho, alto):
        try:
            self.ancho = int(ancho)
            self.alto = int(alto)
            if self.ancho <= 0 or self.alto <= 0:
                raise ValueError("Las dimensiones deben ser enteros positivos")
        except ValueError:
            print("Error: Ingrese solo números enteros positivos")
            self.ancho = 0
            self.alto = 0
    
    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)


def menu():
    while True:
        print("\n1. Calcular área y perímetro")
        print("2. Salir")
        opcion = input("Opción: ")
        
        if opcion == "1":
            try:
                ancho = int(input("Ancho (entero): "))
                alto = int(input("Alto (entero): "))
                
                if ancho <= 0 or alto <= 0:
                    print("Error: Solo valores positivos")
                    continue
                
                rect = Rectangulo(ancho, alto)
                print(f"Área: {rect.area()}")
                print(f"Perímetro: {rect.perimetro()}")
            
            except ValueError:
                print("Error: Ingrese solo números enteros")
        
        elif opcion == "2":
            print("¡Adiós!")
            break
        
        else:
            print("Opción no válida")


if __name__ == "__main__":
    menu()