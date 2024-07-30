#Crea una clase Producto con un método calcular_precio_descuento(). Luego,
#crea clases derivadas como ProductoDescuento, ProductoNormal, etc., que
#implementen este método de manera diferente.


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def calcular_precio_descuento(self):
        raise NotImplementedError("Este método debe ser implementado por las clases derivadas.")

class ProductoDescuento(Producto):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio)
        self.descuento = descuento
    
    def calcular_precio_descuento(self):
        return self.precio * (1 - self.descuento / 100)

class ProductoNormal(Producto):
    def calcular_precio_descuento(self):
        return self.precio  # Sin descuento