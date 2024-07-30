#Imagina que estás trabajando en un programa de gestión de un sistema
#educativo. Tu tarea es diseñar un conjunto de clases orientadas a objetos
#para administrar estudiantes, profesores, asignaturas y calificaciones. Debes
#crear clases como 'Estudiante', 'Profesor', 'Asignatura' y 'Calificacion'.     
#Implementa herencia para representar diferentes niveles de estudiantes,
#como 'EstudianteRegular' y 'EstudianteAvanzado'. Utiliza la composición para
#gestionar la relación entre estudiantes, asignaturas y calificaciones, y
#asegúrate de que el diseño sea versátil para futuras funcionalidades del
#sistema educativo.




class Calificacion:
    def __init__(self, asignatura, nota):
        self.asignatura = asignatura
        self.nota = nota

    def __str__(self):
        return f"{self.asignatura.nombre}: {self.nota}"

class Asignatura:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.asignaturas = []
        self.calificaciones = []

    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def obtener_promedio(self):
        if not self.calificaciones:
            return 0
        total = sum(calificacion.nota for calificacion in self.calificaciones)
        return total / len(self.calificaciones)

    def __str__(self):
        return f"Estudiante: {self.nombre}, Edad: {self.edad}, Promedio: {self.obtener_promedio()}"

class EstudianteRegular(Estudiante):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def detalle(self):
        return f"Estudiante Regular: {self.nombre}, Edad: {self.edad}"

class EstudianteAvanzado(Estudiante):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def detalle(self):
        return f"Estudiante Avanzado: {self.nombre}, Edad: {self.edad}"

class Profesor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return f"Profesor: {self.nombre}, Especialidad: {self.especialidad}"

# Ejemplo de uso
asig_matematicas = Asignatura("Matemáticas")
asig_fisica = Asignatura("Física")

estudiante_1 = EstudianteRegular("Lula", 20)
estudiante_2 = EstudianteAvanzado("Cami", 22)

estudiante_1.agregar_asignatura(asig_matematicas)
estudiante_1.agregar_asignatura(asig_fisica)
estudiante_1.agregar_calificacion(Calificacion(asig_matematicas, 85))
estudiante_1.agregar_calificacion(Calificacion(asig_fisica, 90))

estudiante_2.agregar_asignatura(asig_matematicas)
estudiante_2.agregar_calificacion(Calificacion(asig_matematicas, 95))

profesor_1 = Profesor("Dr. RODRIGUEZ", "Matemáticas")

print(estudiante_1)
print(estudiante_2)
print(profesor_1)
print("\nCalificaciones de Lula:")
for cal in estudiante_1.calificaciones:
    print(cal)
print("\nCalificaciones de Cami:")
for cal in estudiante_2.calificaciones:
    print(cal)




