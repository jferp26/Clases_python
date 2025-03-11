import json
import os



class Agenda:
    def __init__(self,archivo="contactos.json"):
        self.archivo = archivo
        self.contactos = self.cargarcontactos()

    def cargarcontactos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                return json.load(f)
        
        return {}
    
    def mostraragenda(self):
        if self.contactos:
            for nombre, info in self.contactos.items():
                print(f"Nombre: {nombre}")
                print(f"telefono: {info['telefono']}")
                print(f"Email: {info['email']}\n")
        
        else:
            print("la agenda esta vacia")

        
Agenda_test = Agenda()
Agenda_test.mostraragenda()
        

