###Ejercicio 2: Contador de palabras
###Escribe una función que reciba una cadena de texto y devuelva cuántas palabras contiene.
###Luego, crea una clase Texto que use esa función como método y almacene el texto como atributo.

cadena=input("introduzca un texto: ")
def contadordepalabras(cadena):
    texto = cadena.split()
    return len(texto)

class Texto:
    def __init__(self,text):
        self.text = text
    
    def contador(self):
        return contadordepalabras(self.text)

if __name__ == "__main__":
    cadena = input("Introduzca un texto: ")
    funtexto = Texto(cadena)
    print(f"numero de palabras = {funtexto.contador()}")