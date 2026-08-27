from material import Material # Clase padre para todos los materiales de la biblioteca

class Revista(Material): # Clase hija de la clase Material, representa una revista en la biblioteca
    def __init__(self, titulo, autor, precio, es_nuevo, edicion):
        super().__init__(titulo, autor, precio, es_nuevo)
        self.__edicion = edicion
    
    def get_edicion(self): # Obtiene el numero de edicion de la revista
        return self.__edicion

    def set_edicion(self, edicion): # Establece el numero de edicion de la revista
        if edicion < 0:
            raise ValueError("El numero de edicion no puede ser menor a 0")
        else:
            self.__edicion = edicion

    def descripcion(self): # Muestra la descripcion de la revista usando polimorfismo para el llamado de la descripcion de la clase padre Material
        super().descripcion()
        print(f"Edición: {self.__edicion}")