#Crea una clase Usuario con atributos como nombre, email y contraseña.
#Crea métodos para cambiar la contraseña y para mostrar la información del
#usuario

class usuario:
        def __init__(self.nombre,email,contraseña):
        self.nombre=nombre
        self.email=email
        self.contraseña=contraseña

    def cambiar_contraseña(self,nueva_contraseña):
        self.contraseña=nueva_contraseña
    def mostrar_informacion(self):
        print("nombre:",self.nombre)
        print("email:",self.email)
        print("contraseña:",self.contraseña)
        
        
        class usuario:
        def __init__(self, nombre, email, contraseña):
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña

    def cambiar_contraseña(self, nueva_contraseña):
        self.contraseña = nueva_contraseña
    
    def mostrar_informacion(self):
        print("nombre:", self.nombre)
        print("email:", self.email)
        print("contraseña:", self.contraseña)

 
# algo mas.. 
mi_usuario = usuario("luli", "lula.freecat@gmail.com", "passwordfree")

mi_usuario.cambiar_contraseña("newpassword456")

# Display user information
mi_usuario.mostrar_informacion()