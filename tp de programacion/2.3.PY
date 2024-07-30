#Implementa un sistema de gestión de inventario para una tienda que incluya
#clases como Producto, Inventario, Proveedor, etc. El inventario debe ser
#capaz de realizar operaciones como agregar productos, actualizar
#existencias, etc.

class producto:
     def __init__(self, nombre, precio, cantidad):
         self. nombre= nombre
         self.precio=precio
         self.cantidad=cantidad

class inventario:
     def __init__(self, id_producto, precio, entrada, salida):
         id_producto= id_producto
         precio=precio
         entrada= entrada
         salida= salida
         
class proveedor:
     def __init__(self, nombre,contacto, credito_acumulado):
         self.nombre=nombre
         self.contacto=contacto
         self.credito_acumulado
         
class inventario:
     def __init__(self):
        self.productos= {}
        
     def agregar_producto(self, producto):
        if producto.nombre in self.productos:
         print("Error: El producto ya existe en el inventario.")
        else:
         self.productos[producto.nombre] = producto
         
         def actualizar_stock(self, nombre_producto, cantidad):
          if nombre_producto in self.productos:
            self.productos[nombre_producto].cantidad += cantidad
          else:
             print("Error: El producto no existe en el inventario.")

          def mostrar_inventario(self):
            print("Inventario:")
            for nombre, producto in self.productos.items():
             print(f"  - {nombre}: {producto.cantidad} unidades")

# Ejemplo de uso
producto1 = producto("reloj", 20, 50)
producto2 = producto("Pantalla led", 50, 30)
proveedor1 = proveedor("Proveedor A", "123456789")

inventario = inventario()
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.mostrar_inventario()

inventario.actualizar_stock("reloj", 10)
inventario.mostrar_inventario()