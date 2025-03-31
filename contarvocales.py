"""Ejercicio 12: Contador de vocales
Diseña una clase AnalizadorTexto con un atributo para una cadena de texto.
Implementa un método que cuente cuántas vocales (a, e, i, o, u) hay en el texto."""

class AnalizadorTexto:
    def __init__(self, texto):
        self.texto = texto.lower() if texto else ""
    
    def contar_vocales(self):
        vocales = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']
        try:
            if not isinstance(self.texto, str):
                raise TypeError("Error: El texto debe ser una cadena")
            return sum(1 for letra in self.texto if letra in vocales)
        except Exception as e:
            print(f"Error: {e}")
            return 0

def mostrar_menu():
    while True:
        print("\nCONTADOR DE VOCALES")
        print("1. Analizar texto")
        print("2. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                texto = input("Ingrese el texto a analizar: ")
                if not texto.strip():
                    print("Error: No ingresó texto")
                    continue
                
                analizador = AnalizadorTexto(texto)
                total = analizador.contar_vocales()
                print(f"Vocales encontradas: {total}")
            
            elif opcion == 2:
                print("Saliendo del programa...")
                break
            
            else:
                print("Opción no válida")
        
        except ValueError:
            print("Error: Ingrese un número válido")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    mostrar_menu()