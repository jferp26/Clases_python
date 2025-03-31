class Notas:
    def __init__(self,notas):
        self.notas = notas
    def promedio(self):
        try:
            promedio = sum(self.notas)/len(self.notas)
            return promedio
        except:
            ZeroDivisionError
            raise ("No se puede calcular la media sin calificaciones por encima de cero")
    def notamassalta(self):
        try:
                top = max(self.notas)
                return top
        except:
            ZeroDivisionError
            raise ("no se puede hallar la nota mas alta sin notas")





    