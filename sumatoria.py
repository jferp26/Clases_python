"""
Realice un programa que reciba como parámetros 2 números enteros.

La función sumará todos los números entre esos dos números, ambos incluidos.

Finalmente imprimirá en pantalla el número obtenido.
"""


def sumatoria(numero1,numero2):
    sumatorio=[]
    if numero1 > numero2:
        for i in range (numero2,numero1+1):
            sumatorio.append(i)
        return sum(sumatorio)
    
    elif numero2 > numero1:
        for i in range (numero1,numero2+1):
            sumatorio.append(i)
        return sum(sumatorio)
        

print(sumatoria(0,5))
print(sumatoria(4,1))
            
            
        
        
