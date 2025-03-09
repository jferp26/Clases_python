import math

class Lanzamiento:
    alcance=0
    altura_max=0

    def __init__(self, gravedad, angulo, velocidad):
        self.gravedad = gravedad
        self.angulo = angulo
        self.velocidad = velocidad

    def get_gravedad(self):
        return self.gravedad

    def get_angulo(self):
        return self.angulo

    def get_velocidad(self):
        return self.velocidad

    def get_alcance(self):
        return self.alcance

    def get_altura_max(self):
        return self.altura_max

    def set_gravedad(self, gravedad):
        self.gravedad = gravedad

    def set_angulo(self, angulo):
        self.angulo = angulo

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def set_alcance(self,alcance):
        self.alcance=alcance

    def set_altura_max(self,altura_max):
        self.altura_max= altura_max

    def mostrar_parametros(self):
        print(f"Ángulo: {self.get_angulo()} grados")
        print(f"Velocidad: {self.get_velocidad()}")
        print(f"Gravedad: {self.get_gravedad()}")

    def tiro(self):
        angulo_rad = math.radians(self.get_angulo())   # convierte ángulo de grados a radianes 
        self.alcance = (self.get_velocidad()**2) * math.sin(2*angulo_rad) / self.get_gravedad()
        self.altura_max = (self.get_velocidad()**2) * (math.sin(angulo_rad)**2) / (2*self.get_gravedad() )
        print(f"Alcance: {self.get_alcance()} metros")
        print(f"Altura máxima: {self.get_altura_max()} metros")

def menu():
    while True:
        print("### Bienvenido al programa de lanzamiento de misiles de la Armada Española ###")
        print("1. Introducir parámetros de lanzamiento")
        print("2. Salir")
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            angulo = int(input("introduce el ángulo de lanzamiento en grados: "))
            velocidad = int(input("introduce la velocidad de lanzamiento: "))
            gravedad = float(input("introduce la gravedad: "))
            lanzamiento = Lanzamiento(gravedad, angulo, velocidad)
            lanzamiento.mostrar_parametros()
            lanzamiento.tiro()

        elif opcion == 2:
            print("Salir del programa. ¡Hasta luego!")
            break

menu()

  