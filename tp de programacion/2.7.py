#2.7. Crea un simulador de una red social donde los usuarios puedan registrarse,
#agregar amigos, publicar mensajes, etc. Debe haber clases como Usuario,
#Publicación, Comentario, etc.






class Usuario:  
    def __init__(self, nombre, edad):  
        self.nombre = nombre  
        self.edad = edad  
        self.amigos = []  
        self.publicaciones = []  

    def agregar_amigo(self, amigo):  
        if amigo not in self.amigos and amigo != self:  
            self.amigos.append(amigo)  
            amigo.amigos.append(self)  
            print(f"{self.nombre} y {amigo.nombre} son ahora amigos.")  
        else:  
            print(f"No se puede agregar a {amigo.nombre} como amigo.")  

    def publicar(self, contenido):  
        publicacion = Publicacion(contenido, self)  
        self.publicaciones.append(publicacion)  
        print(f"{self.nombre} ha publicado: '{contenido}'")  
        return publicacion  

    def mostrar_publicaciones(self):  
        print(f"Publicaciones de {self.nombre}:")  
        for publicacion in self.publicaciones:  
            print(publicacion)  

    def __str__(self):  
        return self.nombre  


class Publicacion:  
    def __init__(self, contenido, usuario):  
        self.contenido = contenido  
        self.usuario = usuario  
        self.comentarios = []  

    def agregar_comentario(self, comentario):  
        self.comentarios.append(comentario)  
        print(f"Comentario agregado a la publicación de {self.usuario.nombre}: '{comentario.contenido}'")  

    def __str__(self):  
        return f"{self.usuario.nombre} dice: '{self.contenido}' ({len(self.comentarios)} comentarios)"  


class Comentario:  
    def __init__(self, contenido, usuario):  
        self.contenido = contenido  
        self.usuario = usuario  

    def __str__(self):  
        return f"{self.usuario.nombre} comenta: '{self.contenido}'"  


# Ejemplo de uso  
if __name__ == "__main__":  
    # Crear usuarios  
    usuario1 = Usuario("Lula", 32)  
    usuario2 = Usuario("Gonza88", 25)  
    usuario3 = Usuario("Cami27A", 28)  

    # Agregar amigos  
    usuario1.agregar_amigo(usuario2)  
    usuario1.agregar_amigo(usuario3)  
    usuario2.agregar_amigo(usuario3)  

    # Publicar mensajes  
    publicacion1 = usuario1.publicar("¡Hola a todos!")  
    publicacion2 = usuario2.publicar("Hoy, no se olviden de ser felices.")  

    # Agregar comentarios  
    comentario1 = Comentario("¡Hola, Lula!", usuario2)  
    publicacion1.agregar_comentario(comentario1)  

    comentario2 = Comentario("¡Sí, totalmente!", usuario3)  
    publicacion2.agregar_comentario(comentario2)  

    # Mostrar publicaciones  
    usuario1.mostrar_publicaciones()  
    usuario2.mostrar_publicaciones()