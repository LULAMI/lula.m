#Crea una clase abstracta llamada Vehiculo que tenga métodos abstractos
#como acelerar() y frenar(). Luego, crea clases concretas como Coche, Moto,
#Bicicleta, etc., que hereden de Vehiculo y proporcionen implementaciones
#concretas para estos métodos.



from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass

class Coche(Vehiculo):
    def acelerar(self):
        print("El coche está acelerando")

    def frenar(self):
        print("El coche está frenando")

class Moto(Vehiculo):
    def acelerar(self):
        print("La moto está acelerando")

    def frenar(self):
        print("La moto está frenando")

class Bicicleta(Vehiculo):
    def acelerar(self):
        print("La bicicleta está acelerando")

    def frenar(self):
        print("La bicicleta está frenando")

# Ejemplo de uso
mi_coche = Coche("Toyota", "Corolla", "Rojo")
mi_moto = Moto("Honda", "CBR", "Negro")
mi_bicicleta = Bicicleta("Trek", "Mountain Bike", "Azul")

mi_coche.acelerar()
mi_moto.frenar()
mi_bicicleta.acelerar()





