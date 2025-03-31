import random
class Dado:
    def __init__(self,caras_dado):
        self.caras_dado = caras_dado
    
    def tirada(self):
        resultado = random.randint(1,self.caras_dado)
        return resultado
    
    def resultado(self):
        print(self.tirada())


def menu():
    carasvalidas = [2, 4, 6, 8, 10, 12, 20]
    
    while True:
        print("############# TIRAR DADOS ##############")
        print("SELECCIONE LAS CARAS DEL DADO QUE DESEA TIRAR")
        print("2.- DADO DE 2 CARAS")
        print("4.- DADO DE 4 CARAS")
        print("6.- DADO DE 6 CARAS")
        print("8.- DADO DE 8 CARAS")
        print("10.- DADO DE 10 CARAS")
        print("12.- DADO DE 12 CARAS")
        print("20.- DADO DE 20 CARAS")
        print("0.- SALIR")

        try:
            caras = int(input("\nIntroduzca el número de caras del dado a tirar: "))
            
            if caras == 0:
                print("¡HASTA LUEGO!")
                break
                
            if caras not in carasvalidas:
                print(f"Error: El dado de {caras} caras no existe. elije {carasvalidas}")
                continue
                
            dado = Dado(caras)
            resultado = dado.tirada()
            print(f"la tirada del dado de {caras} caras, es: {resultado}")
        except ValueError:
            print("Error: introduce un número entero válido")
            continue

if __name__ == "__main__":
    menu()
    
    
        
