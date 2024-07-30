#Define una clase abstracta llamada Empleado que tenga métodos abstractos
#como calcular_sueldo() y generar_reporte(). Luego, crea clases concretas
#como Desarrollador, Gerente, Contador, etc., que hereden de Empleado y
#proporcionen implementaciones concretas para estos métodos. 
    
from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_sueldo(self):
        pass

    @abstractmethod
    def generar_reporte(self):
        pass

class Desarrollador(Empleado):
    def __init__(self, nombre, salario_base, horas_trabajadas):
        self.nombre = nombre
        self.salario_base = salario_base
        self.horas_trabajadas = horas_trabajadas

    def calcular_sueldo(self):
        return self.salario_base + (self.horas_trabajadas * 20)  # Sueldo base + horas extras

    def generar_reporte(self):
        return f"Reporte de Desarrollador: {self.nombre}, Sueldo: {self.calcular_sueldo()}"

class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bonificaciones):
        self.nombre = nombre
        self.salario_base = salario_base
        self.bonificaciones = bonificaciones

    def calcular_sueldo(self):
        return self.salario_base + self.bonificaciones  # Salario base + bonificaciones

    def generar_reporte(self):
        return f"Reporte de Gerente: {self.nombre}, Sueldo: {self.calcular_sueldo()}"

class Contador(Empleado):
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_sueldo(self):
        return self.salario_base  # Sueldo base

    def generar_reporte(self):
        return f"Reporte de Contador: {self.nombre}, Sueldo: {self.calcular_sueldo()}"

# Ejemplo de uso
desarrollador = Desarrollador("Lula", 3000, 10)
gerente = Gerente("Camila", 5000, 1000)
contador = Contador("Patricio", 4000)

print(desarrollador.generar_reporte())
print(gerente.generar_reporte())
print(contador.generar_reporte())