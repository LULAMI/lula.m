#Imagina que estás desarrollando un sistema de gestión para una empresa de
#comercio electrónico. Tu tarea es diseñar un conjunto de clases orientadas a
#objetos para manejar productos, carritos de compra, usuarios y pedidos.
#Debes crear clases como 'Producto', 'Carrito', 'Usuario' y 'Pedido'. Aplica
#herencia para representar diferentes tipos de usuarios, como 'Cliente' y
#'Administrador'. Utiliza la composición para gestionar la relación entre
#productos y carritos, y asegúrate de que el diseño sea escalable para futuras
#características del comercio electrónico.

class Producto:  
    def __init__(self, nombre, precio, stock):  
        self.nombre = nombre  
        self.precio = precio  
        self.stock = stock  

    def __str__(self):  
        return f"{self.nombre} - Precio: ${self.precio:.2f} - Stock: {self.stock}"  

    def actualizar_stock(self, cantidad):  
        self.stock -= cantidad  


class Carrito:  
    def __init__(self):  
        self.productos = {}  

    def agregar_producto(self, producto, cantidad=1):  
        if producto.stock >= cantidad:  
            if producto in self.productos:  
                self.productos[producto] += cantidad  
            else:  
                self.productos[producto] = cantidad  
            producto.actualizar_stock(cantidad)  
            print(f"Agregado {cantidad} de '{producto.nombre}' al carrito.")  
        else:  
            print(f"No hay suficiente stock para '{producto.nombre}'.")  

    def eliminar_producto(self, producto):  
        if producto in self.productos:  
            cantidad = self.productos[producto]  
            producto.actualizar_stock(-cantidad)  # Vuelve a aumentar el stock  
            del self.productos[producto]  
            print(f"Producto '{producto.nombre}' eliminado del carrito.")  
        else:  
            print(f"El producto '{producto.nombre}' no está en el carrito.")  

    def total(self):  
        return sum(producto.precio * cantidad for producto, cantidad in self.productos.items())  

    def mostrar_contenido(self):  
        print("Contenido del carrito:")  
        for producto, cantidad in self.productos.items():  
            print(f"{producto} - Cantidad: {cantidad}")  
        print(f"Total: ${self.total():.2f}")  


class Usuario:  
    def __init__(self, nombre, email):  
        self.nombre = nombre  
        self.email = email  

    def __str__(self):  
        return f"Usuario: {self.nombre} - Email: {self.email}"  


class Cliente(Usuario):  
    def __init__(self, nombre, email):  
        super().__init__(nombre, email)  
        self.carrito = Carrito()  

    def realizar_pedido(self):  
        if not self.carrito.productos:  
            print("El carrito está vacío. No se puede realizar el pedido.")  
            return  
        pedido = Pedido(self, self.carrito.productos)  
        self.carrito = Carrito()  # Vaciar el carrito después de realizar el pedido  
        print(f"Pedido realizado: {pedido}")  
        return pedido  


class Administrador(Usuario):  
    def __init__(self, nombre, email):  
        super().__init__(nombre, email)  
    
    def agregar_producto(self, nombre, precio, stock, inventario):  
        producto = Producto(nombre, precio, stock)  
        inventario.append(producto)  
        print(f"Producto agregado: {producto}")  


class Pedido:  
    def __init__(self, cliente, productos):  
        self.cliente = cliente  
        self.productos = productos  
        self.numero_pedido = id(self)  # Generar un identificador único usando el id del objeto  

    def __str__(self):  
        return f"Pedido #{self.numero_pedido} por {self.cliente.nombre}"  

# Ejemplo de uso  
if __name__ == "__main__":  
    # Crear un inventario de productos  
    inventario = []  
    
    # Crear un administrador y agregar productos  
    admin = Administrador("lula", "lula.22@tienda.com")  
    admin.agregar_producto("vinotinto", 20000.00, 30000, inventario)  
    admin.agregar_producto("vinochardonnay", 8000.00, 150000, inventario)  
    
    # Crear un cliente  
    cliente = Cliente("Ana", "ana@cliente.com")  
    
    # Mostrar el inventario  
    print("\nInventario:")  
    for producto in inventario:  
        print(producto)  

    # Agregar productos al carrito del cliente  
    cliente.carrito.agregar_producto(inventario[0], 2)  # Agregar 2 vino tinto
    cliente.carrito.agregar_producto(inventario[1], 1)  # Agregar 1 vino chardonnay

    # Mostrar contenido del carrito  
    cliente.carrito.mostrar_contenido()  

    # Realizar un pedido  
    cliente.realizar_pedido()