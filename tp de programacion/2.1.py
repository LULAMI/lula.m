#Crea una clase llamada Producto que tenga atributos como nombre, precio y
#cantidad_disponible. Implementa métodos para actualizar la cantidad
#disponible y para mostrar la información del producto.


class Producto:
    def __init__(self, nombre,precio,cantidad_disponible):
        self.nombre=nombre
        self.precio=precio
        self.cantidad_disponible= cantidad_disponible
        
    
    def actualizar_cantidad(self, cantidad):
        self.cantidad_disponible += cantidad
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Cantidad disponible: {self.cantidad_disponible}")
        
        
producto1 = Producto("mates", 24000, 50)
producto1.mostrar_informacion()

producto1.actualizar_cantidad(-10)
producto1.mostrar_informacion()


    