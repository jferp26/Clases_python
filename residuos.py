"""
Tenemos una empresa de gestión de residuos, que cobra por metro cúbico de basura.

Los precios cobrados son los siguientes:

Madera: 10€ m3

Plástico: 20€ m3

Hospitalarios: 40€ m3

Otros: 30€ m3

Además, el transporte cobrará a razón de 1€ por kilómetro recorrido al ir a buscar los desechos, y 1€ por m3 y kilómetro recorrido a la vuelta.

Realice una aplicación, que pregunte la cantidad de desechos de cada tipo a recoger, además de los Kilómetros y genere un presupuesto.
"""


class Presupuesto:
    def __init__(self, km, madera, plastico, hospitalarios, otros):
        self.madera = madera
        self.plastico = plastico
        self.hospitalarios = hospitalarios
        self.otros = otros
        self.km = km
    
    def calculo_presupuesto(self):
        coste_residuos = (self.madera * 10 + self.plastico * 20 + 
                         self.hospitalarios * 40 + self.otros * 30)
        coste_transporte = self.km + (self.madera + self.plastico + 
                                    self.hospitalarios + self.otros) * self.km
        return coste_residuos + coste_transporte


def menu():
    print("\nPRESUPUESTO DE GESTION DE RESIDUOS")
    
    while True:
        try:
            madera = int(input("Metros cubicos de madera: "))
            plastico = int(input("Metros cubicos de plastico: "))
            hospitalarios = int(input("Metros cubicos de residuos hospitalarios: "))
            otros = int(input("Metros cubicos de otros residuos: "))
            km = int(input("Kilometros de distancia: "))
            
            if madera < 0 or plastico < 0 or hospitalarios < 0 or otros < 0 or km < 0:
                print("Error: Los valores no pueden ser negativos")
                continue
                
            presupuesto = Presupuesto(km, madera, plastico, hospitalarios, otros)
            total = presupuesto.calculo_presupuesto()
            
            print("\nPresupuesto total: €" + str(total))
            break
            
        except ValueError:
            print("Error: Debes introducir numeros enteros\n")


if __name__ == "__main__":
    menu()