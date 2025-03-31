import os
import json

class Tarea:
    def __init__(self,title ="recursos/tareas.json"):
        self.archivo = title
        self.tareas = self.cargar_tareas()
    
    def cargar_tareas(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                return json.loads(f)
        else:
            return {}
    
    def añadir_tarrea(self):
        self.titulo = input(" introduzca el nombre de la tarea: ")
        self.descripcion  = input("Introduce la descripcion de la tarea: ")
        self.completada = "No completada"
        self.tareas[self.titulo]={
            
            "Descripcion" : self.descripcion,
            "Estado" : self.completada
        }
    def eliminar_tarea(self):
        self.delete = input("introduzca la tarea que quiere borrar")
        self.tareas.pop(self.delete)
