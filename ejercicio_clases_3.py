# Crea una clase Profesor que tenga los siguientes atributos:
# -Asignatura 
# -Salario
# El salario de los profesores es un valor tipo fijo float. Crea getter y setter para cada atributo.
# Crea la clase ProfesorAsociado, que hereda de profesor, pero cuyo salario es el resultado de sus horas de clase multiplicado por el precio por hora
# (se puede "harcodear" el precio).

class Profesor:
    def __init__(self, asignatura, salario):
        self._asignatura = asignatura
        self._salario = salario

    def get_asignatura(self):
        return self._asignatura

    def set_asignatura(self, asignatura):
        self._asignatura = asignatura

    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        self._salario = salario


class ProfesorAsociado(Profesor):
    PRECIO_POR_HORA = 20.0  # Precio por hora harcodeado

    def __init__(self, asignatura, horas_clase):
        super().__init__(asignatura, 0)  # El salario inicial es 0 y se calcula
        self._horas_clase = horas_clase

    # Getter y Setter para horas de clase
    def get_horas_clase(self):
        return self._horas_clase

    def set_horas_clase(self, horas_clase):
        self._horas_clase = horas_clase
        self.calcular_salario()  # Recalcula el salario al cambiar las horas

    # Método para calcular el salario basado en las horas de clase
    def calcular_salario(self):
        self._salario = self._horas_clase * ProfesorAsociado.PRECIO_POR_HORA
  