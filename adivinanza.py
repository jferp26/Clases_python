"""
de adivinanza
Crea una clase Adivinanza que genere un número aleatorio entre 1 y 100 (usa random).
Incluye un método que permita al usuario adivinar y devuelva pistas ("más alto" o "más bajo") hasta que acierte.
"""
import random

class Adivinanza:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0
        self.adivinado = False  # Nuevo atributo para controlar el estado
    
    def adivinar(self, numero_usuario):
        self.intentos += 1
        
        try:
            numero = int(numero_usuario)
            
            if numero < 1 or numero > 100:
                return "El número debe estar entre 1 y 100"
            
            if numero < self.numero_secreto:
                return "Más alto"
            elif numero > self.numero_secreto:
                return "Más bajo"
            else:
                self.adivinado = True
                return f"¡Correcto! Lo adivinaste en {self.intentos} intentos"
        
        except ValueError:
            return "Ingresa un número válido"


def jugar():
    juego = Adivinanza()
    print("Adivina el número secreto (entre 1 y 100)")
    
    while True:
        intento = input("Tu adivinanza: ")
        resultado = juego.adivinar(intento)
        print(resultado)
        
        if juego.adivinado:  # Condición simplificada
            break


if __name__ == "__main__":
    jugar()