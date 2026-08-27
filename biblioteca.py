from material import Material

class Biblioteca:
    def __init__(self): # Metodo constructor de la clase Biblioteca 
        self.__materiales = []
    
    def get_materiales(self): # Obtiene la lista de materiales de la biblioteca
        return self.__materiales

    def agregar_material(self, material): # Agrega un material a la lista de materiales de la biblioteca
        self.__materiales.append(material)
        if material in self.__materiales:
            print("Material agregado correctamente")

    def mostrar_catalogo(self): # Muestra el catalogo de materiales de la biblioteca

        for material in self.__materiales:
            material.descripcion()
            print("----------------------------------------")