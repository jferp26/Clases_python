lista2_dimensiones=[[1,2,3,4,5,6],[1,2,3,4,5,6]]

"""
def comprobar_listas(lista1,lista2):
    if len(lista1) == len(lista2):
        for i in range(len(lista1)):
            if lista1[i] !=lista2[i]:
                return " no sin iguales"
            else: 
             return "son iguales"
       
    else:
        return " no sin iguales"

print(comprobar_listas(lista1,lista2))
"""

def comparador(l1,l2):
    if len(l1)!=len(l2):
        return "son diferentes en longitud"
    else:
        for indice in range(len(l1)):
            if l1[indice] != l2[indice]:
                return "son diferentes en elementos"
        return "son iguales"


lista1=[1,2,3,4,5,6]
lista2=[1,2,3,4,5,6]
print(comparador(lista1,lista2))
