#Implementa una clase Aula que tenga una lista de estudiantes y un profesor.
#Usa composición para representar la relación entre un aula y las personas
#que la ocupan.

class Persona:
      def __init__(self, nombre, ID_estudiante):
        self.nombre = nombre
        self.ID_estudiante = ID_estudiante
       
      def mostrar_detalles(self):
           print("Nombre:", self.nombre)
           print("ID_estudiante:", self.ID_estudiante)

class Estudiante(Persona):
    def __init__(self, nombre, ID_estudiante, grado):
      super().__init__(nombre, ID_estudiante)
      self.grado = grado

    def mostrar_detalles(self):
      super().mostrar_detalles()
    print("Grado:",self.grado)

class Profesor(Persona):
  def __init__(self, nombre, ID_estudiante, materia):
    super().__init__(nombre, ID_estudiante)
    self.materia = materia

  def mostrar_detalles(self):
    super().mostrar_detalles()
    print("Materia:", self.materia)

class Aula:
  def __init__(self, nombre):
    self.nombre = nombre
    self.estudiantes = []
    self.profesor = None

  def agregar_estudiante(self, estudiante):
    self.estudiantes.append(estudiante)

  def asignar_profesor(self, profesor):
    self.profesor = profesor

  def mostrar_detalles(self):
    print("Aula:", self.nombre)
    if self.profesor:
      print("Profesor:")
      self.profesor.mostrar_detalles()
    print("Estudiantes:")
    for estudiante in self.estudiantes:
      estudiante.mostrar_detalles()

# Ejemplo de uso
estudiante1 = Estudiante("Arguello", 10, 5)
estudiante2 = Estudiante("Marciel", 11, 6)
profesor1 = Profesor("Campos", 35, "Matemáticas")

aula1 = Aula("A1")
aula1.agregar_estudiante(estudiante1)
aula1.agregar_estudiante(estudiante2)
aula1.asignar_profesor(profesor1)

aula1.mostrar_detalles()