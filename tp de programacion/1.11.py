#Crea una clase abstracta llamada Animal que tenga métodos abstractos
#como hacer_sonido() y moverse(). Luego, crea clases concretas como Perro,
#Gato, Pájaro, etc., que hereden de Animal y proporcionen implementaciones
#concretas para estos métodos.


from abc import abstractmethod


class Animal(abstractmethod):  
    abstractmethod  
    def hacer_sonido(self):  
        pass  
    
    abstractmethod  
    def moverse(self):  
        pass  

class Perro(Animal):  
    def hacer_sonido(self):  
        return "¡Guau!"  
    
    def moverse(self):  
        return "El perro corre con energía."  

class Gato(Animal):  
    def hacer_sonido(self):  
        return "¡Miau!"  
    
    def moverse(self):  
        return "El gato se mueve sigilosamente."  

class Pajaro(Animal):  
    def hacer_sonido(self):  
        return "¡Pío!"  
    
    def moverse(self):  
        return "El pájaro vuela alto."  

# Ejemplo de uso  
def main():  
    animals = [Perro(), Gato(), Pajaro()]  
    
    for animal in animals:  
        print(f"Sonido: {animal.hacer_sonido()}")  
        print(f"Movimiento: {animal.moverse()}")  
        print("-" * 20)  

if __name__ == "__main__":  
    main() 