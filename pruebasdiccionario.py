"""
hacer una aplicacion para tener
 una agenda de telefono, los telefonos se guardaran
   en un diccionario con clave: nombre del contacto y valor:
telefono
necesitamos los siguientes metodos:
 __init__
 metodo para introducir un contacto
 metodo para borrar contacto por nombre
 metodo para buacar contacto por nombre
 metodo para mostrar toda la agenda
 """

class Agenda:
    def __init__(self):
        self.agenda={}
   
    def añadir_contacto(self):
        self.nombre=input("introduzca el Nombre del contacto: ")
        self.numero=int(input("introduzca el numero de telefono: "))
        self.agenda.update({self.nombre:self.numero})
        print(f"Usted ha añadido el contacto {self.nombre} con el numero de telefono {self.numero} a la agenda")
   
    def borrar_contacto(self):
        self.nombre=input("introduzca el contacto que desea borrar: ")
        del self.agenda [self.nombre]
        print(f"Usted ha eliminado el contacto {self.nombre} de la agenda")
    
    def buscar_contacto(self):
        self.nombre=input("introduzca el contacto que desea buscar: ")
        self.telefono = self.agenda.get(self.nombre)
        print(f"El numero de telefono de {self.nombre} es {self.telefono}")
    


    