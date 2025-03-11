class Agenda:
    def __init__(self):
        self.agenda = {}

    def añadir_contacto(self, nombre, numero):
        self.agenda[nombre] = numero
        print(f"Se ha añadido el contacto {nombre} con el número {numero}.")

    def borrar_contacto(self, nombre):
        if nombre in self.agenda:
            self.agenda.pop(nombre)
            print(f"Se ha eliminado el contacto {nombre}.")
        else:
            print(f"El contacto {nombre} no existe en la agenda.")

    def buscar_contacto(self, nombre):
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
            print("Bienvenido a la Agenda")
            print("Seleccione la acción que desea realizar")
            print(" 1.- Añadir contacto")
            print(" 2.- Buscar contacto")
            print(" 3.- Borrar contacto")
            print(" 4.- Mostrar Agenda")
            print(" 5.- Salir de la Agenda")
            accion = int(input("Introduzca la opción deseada: "))
            if accion == 1:
                nombre = input("Introduzca el nombre del contacto: ")
                numero = input("Introduzca el número de teléfono: ")
                self.añadir_contacto(nombre, numero)
            elif accion == 2:
                nombre = input("Introduzca el nombre del contacto que desea buscar: ")
                self.buscar_contacto(nombre)
            elif accion == 3:
                nombre = input("Introduzca el nombre del contacto que desea borrar: ")
                self.borrar_contacto(nombre)
            elif accion == 4:
                self.mostrar_agenda()
            elif accion == 5:
                print("Usted ha salido de la agenda.")
                break

mi_agenda = Agenda()
mi_agenda.menu_agenda()
