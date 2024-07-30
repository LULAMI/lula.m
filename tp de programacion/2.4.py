#Crea un sistema de gestión de tareas que permita a los usuarios agregar,
#eliminar y actualizar tareas. Debe haber clases como Tarea, ListaTareas, etc.


class Tarea:  
    def __init__(self, descripcion):  
        self.descripcion = descripcion  
        self.completada = False  

    def completar(self):  
        self.completada = True  

    def __str__(self):  
        estado = "completada" if self.completada else "pendiente"  
        return f"[{estado}] {self.descripcion}"  
    
    class ListaTareas:  
      def __init__(self):  
        self.tareas = []  

    def agregar_tarea(self, descripcion):  
        nueva_tarea = Tarea(descripcion)  
        self.tareas.append(nueva_tarea)  
        print(f"Tarea agregada: {descripcion}")  
        
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, nombre_tarea):
      
      self.tareas = [tarea for tarea in self.tareas if tarea.nombre != nombre_tarea]

    def actualizar_tarea(self, nombre_tarea, nueva_descripcion):
     for tarea in self.tareas:
      if tarea.nombre == nombre_tarea:
        tarea.descripcion = nueva_descripcion
        return
    print("Error: La tarea no existe.")

def mostrar_tareas(self):
    print("Lista de Tareas:")
    for tarea in self.tareas:
      tarea.mostrar_detalles()

# Ejemplo de uso
tarea1 = Tarea("Comprar leche", "Ir al supermercado y comprar leche")
tarea2 = Tarea("Estudiar para el examen", "Repasar los apuntes y hacer ejercicios")

lista_tareas =tareas()
lista_tareas.agregar_tarea(tarea1)
lista_tareas.agregar_tarea(tarea2)
lista_tareas.mostrar_tareas()

lista_tareas.eliminar_tarea("Comprar leche")
lista_tareas.mostrar_tareas()

lista_tareas.actualizar_tarea("Estudiar para el examen", "Hacer un repaso general")
lista_tareas.mostrar_tareas()


