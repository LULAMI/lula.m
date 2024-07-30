#Imagina que estás desarrollando un sistema de gestión para una compañía
#de transporte. Tu objetivo es diseñar un conjunto de clases orientadas a
#objetos para manejar vehículos, rutas, conductores y clientes. Debes crear
#clases como 'Vehiculo', 'Ruta', 'Conductor' y 'Cliente'. Implementa herencia
#para representar diferentes tipos de vehículos, como 'Automovil' y 'Camion'.
#Utiliza la composición para gestionar la relación entre rutas, conductores y
#clientes, y asegúrate de que el diseño sea escalable para futuras
#funcionalidades del sistema de transporte.


class Vehiculo:  
    def __init__(self, marca, modelo, año, capacidad):  
        self.marca = marca  
        self.modelo = modelo  
        self.año = año  
        self.capacidad = capacidad  

    def __str__(self):  
        return f"{self.marca} {self.modelo} ({self.año}) - Capacidad: {self.capacidad}"  


class Automovil(Vehiculo):  
    def __init__(self, marca, modelo, año, capacidad, numero_asientos):  
        super().__init__(marca, modelo, año, capacidad)  
        self.numero_asientos = numero_asientos  

    def __str__(self):  
        return f"{super().__str__()} - Asientos: {self.numero_asientos}"  


class Camion(Vehiculo):  
    def __init__(self, marca, modelo, año, capacidad, peso_maximo):  
        super().__init__(marca, modelo, año, capacidad)  
        self.peso_maximo = peso_maximo  

    def __str__(self):  
        return f"{super().__str__()} - Peso Máximo: {self.peso_maximo}"  


class Conductor:  
    def __init__(self, nombre, licencia, vehiculo=None):  
        self.nombre = nombre  
        self.licencia = licencia  
        self.vehiculo = vehiculo  

    def asignar_vehiculo(self, vehiculo):  
        self.vehiculo = vehiculo  

    def __str__(self):  
        vehiculo_info = self.vehiculo.__str__() if self.vehiculo else "Sin vehículo asignado"  
        return f"{self.nombre} - Licencia: {self.licencia}, Vehículo: {vehiculo_info}"  


class Cliente:  
    def __init__(self, nombre, contacto):  
        self.nombre = nombre  
        self.contacto = contacto  

    def __str__(self):  
        return f"{self.nombre} - Contacto: {self.contacto}"  


class Ruta:  
    def __init__(self, nombre, origen, destino):  
        self.nombre = nombre  
        self.origen = origen  
        self.destino = destino  
        self.conductor = None  
        self.cliente = None  

    def asignar_conductor(self, conductor):  
        self.conductor = conductor  

    def asignar_cliente(self, cliente):  
        self.cliente = cliente  

    def __str__(self):  
        conductor_info = self.conductor.__str__() if self.conductor else "Sin conductor asignado"  
        cliente_info = self.cliente.__str__() if self.cliente else "Sin cliente asignado"  
        return f"Ruta: {self.nombre} - De: {self.origen} A: {self.destino} | {conductor_info} | {cliente_info}"  


# Ejemplo de uso  
if __name__ == "__main__":  
    # Crear vehículos  
    auto1 = Automovil("Toyota", "Corolla", 2020, 5, 5)  
    camion1 = Camion("Mercedes", "Atego", 2018, 12, 3000)  

    # Crear conductores  
    conductor1 = Conductor("Juan Pérez", "ABCD1234")  
    conductor1.asignar_vehiculo(auto1)  

    conductor2 = Conductor("María López", "EFGH5678")  
    conductor2.asignar_vehiculo(camion1)  

    # Crear clientes  
    cliente1 = Cliente("Carlos", "carlos@example.com")  
    cliente2 = Cliente("Ana", "ana@example.com")  

    # Crear rutas  
    ruta1 = Ruta("Ruta 1", "Ciudad A", "Ciudad B")  
    ruta1.asignar_conductor(conductor1)  
    ruta1.asignar_cliente(cliente1)  

    ruta2 = Ruta("Ruta 2", "Ciudad C", "Ciudad D")  
    ruta2.asignar_conductor(conductor2)  
    ruta2.asignar_cliente(cliente2)  

    # Mostrar información  
    print("\nVehículos:")  
    print(auto1)  
    print(camion1)  

    print("\nConductores:")  
    print(conductor1)  
    print(conductor2)  

    print("\nClientes:")  
    print(cliente1)  
    print(cliente2)  

    print("\nRutas:")  
    print(ruta1)  
    print(ruta2)
