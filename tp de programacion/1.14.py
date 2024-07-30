# Define una clase Playlist que tenga una lista de canciones. Usa composición
#para representar la relación entre una lista de reproducción y las canciones
#que la componen.

class Cancion:
    def __init__(self, nombre, artista, duracion):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion

    def mostrar_detalles(self):
        print("Nombre:", self.nombre)
        print("Artista:", self.artista)
        print("Duración:", self.duracion)

class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def mostrar_canciones(self):
        print("Playlist:", self.nombre)
        for cancion in self.canciones:
            cancion.mostrar_detalles()

# Ejemplo de uso
cancion1 = Cancion("Siesta de Verano", "Luciano Pereyra, Luis Fonsi", "3:08")
cancion2 = Cancion("DPM", "Kany Garcia", "3:01")