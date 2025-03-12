

class Agenda:
    def __init__(self):
        self.agenda = {}

    def añadir_contacto(self):
        nombre = input("Introduzca el nombre del contacto: ")
        numero = input("Introduzca el número de teléfono: ")
        self.agenda[nombre] = numero
        print(f"Se ha añadido el contacto {nombre} con el número {numero}.")

    def borrar_contacto(self):
        nombre = input("Introduzca el nombre del contacto que desea borrar: ")
        if nombre in self.agenda:
            self.agenda.pop(nombre)
            print(f"Se ha eliminado el contacto {nombre}.")
        else:
            print(f"El contacto {nombre} no existe en la agenda.")

    def buscar_contacto(self):
        nombre = input("Introduzca el nombre del contacto que desea buscar: ")
        if nombre in self.agenda:
            print(f"El número de {nombre} es {self.agenda[nombre]}.")
        else:
            print(f"El contacto {nombre} no existe en la agenda.")

    def mostrar_agenda(self):
        if not self.agenda:
            print("La agenda está vacía.")
        else:
            print("Contactos en la agenda:")
            for nombre, numero in self.agenda.items():
                print(f"{nombre}: {numero}")
    def menu_agenda(self):

        while True:
           print("bienvenido a Agenda")
           print("Seleccione la accion que desea realizar")
           print(" 1.- Añadir contacto")
           print(" 2.- buscar contacto")
           print(" 3.- borrar contacto")
           print(" 4.- Mostrar Agenda")
           print(" 5.- Salir de la Agenda")
           self.accion=int(input("Introduzca la opccion deseada: "))
           if self.accion == 1:
               mi_agenda.añadir_contacto()
           elif self.accion == 2:
               mi_agenda.buscar_contacto()
           elif self.accion == 3:
               mi_agenda.borrar_contacto()
           elif self.accion == 4:
               mi_agenda.mostrar_agenda()
           elif self.accion == 5:
               print("Usted ha salido de la agenda")
               break

mi_agenda = Agenda()
mi_agenda.menu_agenda()