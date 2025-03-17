class Calculadora:
    
    def __init__(self,numero1,numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    def suma(self):
      return self.numero1+self.numero2
    
    def resta(self):
      return self.numero1-self.numero2
  
    def multiplicacion(self):
      return self.numero1*self.numero2
  
    def division(self):
      return self.numero1/self.numero2
  
def menu():
    while True:
     print("CALCULADORA")
     print("1.- SUMA")
     print("2.- RESTA")
     print("3.- MULTIPLICACION")
     print("4.- DIVISION")
     operacion=int(input("introduzca la operacion a realizar:"))
     num1 = int(input("introduzca el primer numero: "))
     num2 = int(input("introduzca el segundo numero: "))
     if operacion == 1:
         calculo=Calculadora(num1,num2)
         Calculadora.suma()
     
          
     
          
        
menu()         
    
    
    
        
        
        
        
