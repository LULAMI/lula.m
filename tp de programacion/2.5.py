#Desarrolla un simulador de una ciudad donde puedas controlar aspectos
#como la población, la economía, la seguridad, etc. Crea clases como
#Ciudadano, Edificio, Vehículo, etc.





import random

class Ciudadano:
  def __init__(self, nombre, edad, trabajo):
    self.nombre = nombre
    self.edad = edad
    self. trabajo=trabajo

class Edificio:
  def __init__(self, tipo, capacidad):
    self.tipo = tipo
    self.capacidad = capacidad
    self.ocupantes = 0
    
class Vehiculo:
      def __init__(self, tipo):
        self.tipo = tipo

class Ciudad:
  def __init__(self, nombre):
    self.nombre = nombre
    self.poblacion = []
    self.edificios = []
    self.vehiculos = []
    self.dinero = 1000

  def agregar_ciudadano(self, ciudadano):
    self.poblacion.append(ciudadano)

  def construir_edificio(self, edificio):
    self.edificios.append(edificio)

  def comprar_vehiculo(self, vehiculo):
    self.vehiculos.append(vehiculo)

  def simular_dia(self):
    # Simular trabajo y generar ingresos
    for ciudadano in self.poblacion:
      if ciudadano.trabajo:
        self.dinero += random.randint(10, 50)

    # Simular gastos
    for edificio in self.edificios:
      self.dinero -= random.randint(5, 20)

    # Mostrar información de la ciudad
    print(f"Ciudad: {self.nombre}")
    print(f"Población: {len(self.poblacion)}")
    print(f"Dinero: {self.dinero}")

# Ejemplo de uso
ciudad = Ciudad("Buenos Aires")

ciudadano1 = Ciudadano("lula", 30, "Programador")
ciudadano2 = Ciudadano("Camila", 25, "Doctora")
ciudad.agregar_ciudadano(ciudadano1)
ciudad.agregar_ciudadano(ciudadano2)

edificio1 = Edificio("Casa", 4)
edificio2 = Edificio("Hospital", 20)
ciudad.construir_edificio(edificio1)
ciudad.construir_edificio(edificio2)

vehiculo1 = Vehiculo("Coche")
ciudad.comprar_vehiculo(vehiculo1)

for dia in range(10):
  ciudad.simular_dia()