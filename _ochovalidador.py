class Validador:
    def __init__(self,contraseña):
        self.contraseña = contraseña
    
    def validarcontraseña(self):
        if len(self.contraseña) == 8:
            tienemayuscula = any(letra.isupper() for letra in self.contraseña)
            tieneminuscula = any(letra.islower() for letra in self.contraseña)
            tienenumero = any(letra.isdigit() for letra in self.contraseña)
            if tienemayuscula and tieneminuscula and tienenumero:
                return True
    
    def resultado_contraseña(self):
        if self.validarcontraseña() == True:
            return f"la contraseña {self.contraseña} es valida"


validator = Validador("Pepito33")
print(validator.resultado_contraseña())

