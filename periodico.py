from material import Material # Clase padre para todos los materiales de la biblioteca

class Periodico(Material): # Clase hija de la clase Material, representa un periodico en la biblioteca
    def __init__(self, titulo, autor, precio, es_nuevo, fecha_publicacion):
        super().__init__(titulo, autor, precio, es_nuevo)
        self.__fecha_publicacion = fecha_publicacion

    def get_fecha_publicacion(self):
        return self.__fecha_publicacion

    def set_fecha_publicacion(self, fecha_publicacion): # Establece la fecha de publicacion del periodico
        self.__fecha_publicacion = fecha_publicacion

    def descripcion(self): # Muestra la descripcion del periodico usando polimorfismo para el llamado de la descripcion de la clase padre Material
        super().descripcion()
        print(f"Fecha de publicacion: {self.__fecha_publicacion}")