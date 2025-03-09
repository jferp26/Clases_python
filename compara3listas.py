
lista1=[1,2,3,4,5,6]
lista2=[1,2,3,4,5,6]
lista3=[]

def comparador(l1,l2,l3):
    if len(l1)!=len(l2):
        return "son diferentes en longitud"
    elif len(l1)!=len(l3):
        return "son diferentes en longitud"
    else:
        for indice in range(len(l1)):
            if l1[indice] != l2[indice]:
                return "son diferentes en elementos"
            elif l1[indice] != l3[indice]:
                return "son diferentes en elementos"
        return "son iguales"
while True:
    x=int(input("escriba un numero para añadir a la lista 3, y para salir escriba -000000"))
    if x!=000000:
        lista3.append(x)
    else:
        break


print(comparador(lista1,lista2,lista3))