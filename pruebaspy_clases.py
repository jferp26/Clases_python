class militar:
    empleo="Aspirante"
    nombre="USTED!!!"
    edad=18
    años=""

    def __init__(self):
        pass
    def saludo(self):
        print ("¡a sus ordenes buenos dias!")
    def dalenombre(self,name):
        self.nombre=name
    
    def dimenombre(self):
        print(f"El militar se llama {self.nombre}")

    def daleempleo(self,rank):
        self.empleo=rank

    def dimeempleo(self):
        print(f"su militar es {self.empleo}")

    def daleedad(self,age):
        self.edad=age

    def dimeedad(self):
        print(f"la edad del militar es:{self.edad}")
    def cumple(self):
        self.edad+=1
    




militar1=militar()

militar1.dalenombre("maverick")
militar1.daleempleo("Capitan de corneta")
militar1.daleedad(21)

militar1.dimenombre()
militar1.dimeempleo()
militar1.dimeedad()
militar1.cumple()
militar1.dimeedad()
