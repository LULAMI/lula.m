class Estudiante:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self._promedio = promedio  # Atributo privado para controlar el acceso

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Promedio: {self.promedio}")

    def actualizar_promedio(self, nuevo_promedio):
        if 0 <= nuevo_promedio <= 10:  # Validación del rango del promedio
            self._promedio = nuevo_promedio
        else:
            print("El promedio debe estar entre 0 y 10.")

    def incrementar_edad(self):
        self.edad += 1

    @property
    def promedio(self):
        return self._promedio

    @promedio.setter
    def promedio(self, nuevo_promedio):
        self.actualizar_promedio(nuevo_promedio)

# Ejemplo de uso:
estudiante1 = Estudiante("Juan Pérez", 18, 8.5)
estudiante1.mostrar_informacion()

estudiante1.actualizar_promedio(9.2)
estudiante1.mostrar_informacion()

estudiante1.incrementar_edad()
estudiante1.mostrar_informacion()

# Usando la propiedad promedio
print(estudiante1.promedio)  # Obtener el promedio
estudiante1.promedio = 9.5  # Asignar un nuevo promedio
print(estudiante1.promedio)