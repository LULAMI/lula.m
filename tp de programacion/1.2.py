#Crea una clase Persona con atributos nombre y edad. Crea un método para
#imprimir los datos de la persona.

from __future__ import print_function
class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

def presentarse(self):
        print("Hola, soy", self.nombre, "y tengo", self.edad, "años.")