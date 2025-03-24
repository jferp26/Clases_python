###Ejercicio 3: Lista de números pares
###Crea una clase Numeros con un atributo que sea una lista de enteros.
###Incluye un método que devuelva solo los números pares de esa lista.

class Numeros:
    def __init__(self,lista):
        self.lista = lista
        
    def listapares(self):
        pares=[]
        for i in self.lista:
            if i%2 == 0:
                pares.append(i)
            else:
                continue
        return pares
    
if __name__== "__main__":
    numeritos=Numeros([1,2,3,4,5,6,7,8,9,0,10,11,12,22223333444455556667888,13,14,15,16,17,18])
    print(numeritos.listapares())
