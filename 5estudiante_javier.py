###Ejercicio 5: Gestión de estudiantes
###Crea una clase Estudiante con atributos para nombre, edad y calificación.
###Implementa métodos getter y setter, y un método que determine si el estudiante aprobó (calificación 
###mayor o igual a 6).
###

class Estudiante:
    def __init__(self,nombre,edad,calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion
    
    def set_nombre(self,nombre):
        self.nombre = nombre
    
    def set_edad(self,edad):
        self.edad = edad
    
    def set_calificacion(self,calificacion):
        self.calificacion = calificacion
    
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_calificacion(self):
        return self.calificacion
    
    def aprobado(self):
        if self.calificacion >=6:
            return "aprobado"
        else:
            return "suspenso"


if __name__== "__main__":
    
    pepito = Estudiante("juan",18,5)
    print(pepito.aprobado())