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
    
    def buscarcontactos(self):
        nombre= str.upper(input("introduzca el nombre a buscar: "))
        if nombre in self.contactos.items():
                info = self.contactos[nombre]
                print(f"Nombre: {nombre}")
                print(f"telefono: {info['telefono']}")
                print(f"Email: {info['email']}\n")
        
        else:
            print("contacto no encontrado")

    def borrarcontacto(self):
        nombre= str.title(input("introduzca el nombre a borrar: "))
        if nombre in self.contactos.items():
                self.contactos.pop(nombre)
              #  del self.contactos[nombre]
                print(f"el contaco {nombre} se ha borrado")
        else:
            print("contacto no encontrado")
    

    def añadircontacto(self):
        nombre = input("Introduzca el nombre del contacto: ")
        telefono = input("Introduzca el número de teléfono: ")
        email  = input("Introduzca el número de Email: ")
        self.contactos[nombre] = {"telefono": telefono , "email": email}
        print(f"Se ha añadido el contacto {nombre} con el número {telefono} y el email{email}.")
    
    def guardaragenda(self):
         with open(self.archivo,"w") as f:
              json.dump(self.contactos, f, indent=4)
              
#__name__ nombre del archivo que no se ejecuta el primero
#__main__ archivo que se ejecuta en primer plano
def menu():
    pass
if __name__=="__main__":
     menu()
        
Agenda_test = Agenda()
Agenda_test.mostraragenda()
        

