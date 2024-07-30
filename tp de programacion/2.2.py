#Desarrolla un juego de simulación de vida donde los "seres" pueden ser
#plantas, animales, personas, etc. Cada ser debe tener atributos como
#energía, salud, edad, etc., y comportamientos específicos según su tipo

import random

class Ser:
  def __init__(self, energia, salud, edad):
    self.energia = energia
    self.salud = salud
    self.edad = edad

  def esta_vivo(self):
    return self.energia > 0 and self.salud > 0

class Planta(Ser):
  def __init__(self, energia, salud, edad):
    super().__init__(energia, salud, edad)

  def fotosintesis(self):
    self.energia += 10
    print("La planta realiza la fotosíntesis y ganar energía.")

class Animal(Ser):
  def __init__(self, energia, salud, edad):
    super().__init__(energia, salud, edad)

  def comer(self):
    self.energia += 5
    print("El animal come y gana energía.")

  def moverse(self):
    self.energia -= 2
    print("El animal se mueve y gasta energía.")

class Persona(Animal):
  def __init__(self, energia, salud, edad, nombre):
    super().__init__(energia, salud, edad)
    self.nombre = nombre

  def trabajar(self):
    self.energia -= 5
    print(f"{self.nombre} trabaja, ganar dinero y compra comida para ganar  energía.")

  def dormir(self):
    self.energia += 10
    print(f"{self.nombre} duerme y gana energía.")

# Ejemplo de uso
planta = Planta(50, 80, 2)
animal = Animal(70, 90, 5)
persona = Persona(80, 75, 30, "LULA")

while planta.esta_vivo():
  planta.fotosintesis()
  planta.edad += 1
  print(f"Energía de la planta: {planta.energia}, Edad: {planta.edad}")

while animal.esta_vivo():
  animal.comer()
  animal.moverse()
  animal.edad += 1
  print(f"Energía del animal: {animal.energia}, Edad: {animal.edad}")

while persona.esta_vivo():
      persona.trabajar()
  persona.dormir()
  persona.edad += 1
  print(f"Energía de {persona.nombre}: {persona.energia}, Edad: {persona.edad}")