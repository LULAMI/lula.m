#Crea una clase CarritoCompra que tenga una lista de productos. Usa
#agregación para representar la relación entre un carrito de compra y los
#productos que contiene.

class Producto:
    def __init__(self, nombre,precio):
        self.nombre=nombre
        self.precio=precio
    
class CarritoCompra:
    def __init__(self):
      self.productos= []
    
    def agregar_productos(self, producto):
        self.productos.append(producto)
        
    def mostrar_productos(self):
        print("CarritoCompra:")
        for producto in self.agregar_productos:
            producto.mostrar_detalles()
            
            
            
 producto1 = Producto("Camiseta", 20)
producto2 = Producto("Pantalón", 50)

mi_carrito = CarritoCompra()
mi_carrito.agregar_producto(producto1)
mi_carrito.agregar_producto(producto2)

mi_carrito.mostrar_productos()