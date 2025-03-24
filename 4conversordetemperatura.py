###Ejercicio 4: Conversor de temperaturas
###Diseña una clase ConversorTemperatura con métodos para convertir de Celsius a Fahrenheit y viceversa.
###Usa un constructor para inicializar una temperatura base.

class Conversor_de_Temperatura:
    def __init__(self,tempbase):
        self.tempbase=tempbase

    def pasar_celsius(self):
        fahrenheit= self.tempbase*1.8 +32
        return fahrenheit
    
    def pasar_fahrenheit(self):
        celsius =  (self.tempbase-32)/1.8
        return celsius
def menu():

    
    while True:
        print("CONVERSOR DE TEMPERATURA")
        temp_base = float(input("INTRODUCE LA TEMPERATURA A CONVERTIR: "))
        conversor = Conversor_de_Temperatura(temp_base)
        print("1. CONVERTIR DE CELSIUS A FARENHEIT")
        print("2. CONVERTIR DE FARENHEIT A CELSIUS")
        print("3. SALIR")
        
        opcion = input("SELECCIONA UNA OPCION: ")
        
        if opcion == "1":
            print(f"{conversor.tempbase}°C = {conversor.pasar_celsius()}°F")
        elif opcion == "2":
            print(f"\{conversor.tempbase}°F = {conversor.pasar_fahrenheit()}°C")
        elif opcion == "3":
            print("¡HASTA LUEGO!")
            break
if __name__ == "__main__":
    menu()