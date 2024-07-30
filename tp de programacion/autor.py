class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self._paginas = paginas  # El guion bajo indica que es un atributo privado

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self._paginas}")

    def cambiar_autor(self, nuevo_autor):
        self.autor = nuevo_autor
        print("Autor cambiado correctamente.")

    def agregar_paginas(self, paginas_adicionales):
        if paginas_adicionales > 0:
            self._paginas += paginas_adicionales
            print("Páginas agregadas correctamente.")
        else:
            print("El número de páginas a agregar debe ser positivo.")

# Ejemplo de uso:
libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 867)
libro1.mostrar_informacion()
libro1.cambiar_autor("Otro Autor")
libro1.mostrar_informacion()
libro1.agregar_paginas(100)
libro1.mostrar_informacion()