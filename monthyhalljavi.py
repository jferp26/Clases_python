class concurso:
    
    aciertos=0
    fallos=0
    aciertos_c=0
    fallos_c=0
    puertas=["gana","pierde","pierde"]
    
    def __init__(self,iteraciones):
        self.iteraciones=iteraciones
        
    def get_iteraciones(self):
        return self.iteraciones
    
    def set_iteraciones(self,iteraciones):
        self.iteraciones=iteraciones
        
    def concursar(self,):
        import random
        for i in range(self.get_iteraciones):
            random.shuffle(self.puertas)
            eleccion_jugada=random.choice(self.puertas)
            self.puertas.remove(eleccion_jugada) 
            if eleccion_jugada== "gana":
                self.aciertos+=1
            else: self.fallos_c+=1
        return (self.aciertos,self.fallos_c,self.get_iteraciones)
            
concurso(200)




        
