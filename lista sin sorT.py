#lista sin sorT

def ordenar_sin_sort(lista):
    for i in range(0,len(lista)):
        for j in range (i + 1, len(lista)):
            if lista[i]>lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista


print(ordenar_sin_sort([8,8,5,9,62,21,4,6,3,1,7,9]))
        
class Ordenador:
    def __init__(self,lista):
        self.lista=lista
    
    
    def ordenar_sin_sort(self.lista):
        for i in range(0,len(self.lista)):
            for j in range (i + 1, len(self.lista)):
                if self.lista[i]>self.lista[j]:
                    self.lista[i],self.lista[j]=self.lista[j],self.lista[i]
        return self.lista
        