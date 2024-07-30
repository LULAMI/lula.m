#Implementa un sistema de reservas para un cine que permita a los usuarios
#reservar asientos para películas. Debe haber clases como Pelicula, SalaCine,
#Reserva, etc.


class Pelicula:  
    def __init__(self, titulo, duracion, clasificacion):  
        self.titulo = titulo  
        self.duracion = duracion  # en minutos  
        self.clasificacion = clasificacion  # Ej: "PG-13", "R", etc.  

    def __str__(self):  
        return f"{self.titulo} (Duración: {self.duracion} min, Clasificación: {self.clasificacion})"  


class Asiento:  
    def __init__(self, fila, numero):  
        self.fila = fila  
        self.numero = numero  
        self.reservado = False  

    def reservar(self):  
        self.reservado = True  

    def liberar(self):  
        self.reservado = False  

    def __str__(self):  
        estado = "Reservado" if self.reservado else "Disponible"  
        return f"Asiento {self.fila}{self.numero}: {estado}"  


class SalaCine:  
    def __init__(self, nombre, filas, asientos_por_fila):  
        self.nombre = nombre  
        self.asientos = [[Asiento(chr(65 + fila), numero + 1) for numero in range(asientos_por_fila)] for fila in range(filas)]  

    def mostrar_asientos(self):  
        for fila in self.asientos:  
            for asiento in fila:  
                print(asiento)  
            print()  # Espacio entre filas  

    def reservar_asiento(self, fila, numero):  
        if self.asientos[fila][numero - 1].reservado:  
            print("El asiento ya está reservado.")  
            return False  
        else:  
            self.asientos[fila][numero - 1].reservar()  
            print("Asiento reservado con éxito.")  
            return True  


class Reserva:  
    def __init__(self, pelicula, sala, fila, numero):  
        self.pelicula = pelicula  
        self.sala = sala  
        self.fila = fila  
        self.numero = numero  
        self.confirmada = False  

    def confirmar_reserva(self):  
        if self.sala.reservar_asiento(self.fila, self.numero):  
            self.confirmada = True  
            print(f"Reserva confirmada para {self.pelicula.titulo} en el asiento {self.sala.asientos[self.fila][self.numero - 1].__str__()}.")  
        else:  
            print("No se pudo confirmar la reserva.")  


# Ejemplo de uso  
if __name__ == "__main__":  
    # Crear una película  
    pelicula1 = Pelicula("Inception", 148, "PG-13")  
    
    # Crear una sala de cine  
    sala1 = SalaCine("Sala 1", 5, 10)  # 5 filas, 10 asientos por fila  
    
    # Mostrar asientos disponibles  
    print("Estado de asientos:")  
    sala1.mostrar_asientos()  
    
    # Crear una reserva  
    reserva1 = Reserva(pelicula1, sala1, 0, 1)  # Reserva en fila 0, asiento 1  
    reserva1.confirmar_reserva()  
    
    # Mostrar estado de asientos después de la reserva  
    print("\nEstado de asientos después de la reserva:")  
    sala1.mostrar_asientos() 