class Material: # Clase padre de las revistas, libros y periodicos de la biblioteca

    def __init__(self, titulo, autor, precio, es_nuevo): # Metodo constructor de la clase Material
        self.__titulo = titulo
        self.__autor = autor
        self.__precio = precio
        self.__es_nuevo = True if es_nuevo else False

    def get_precio(self): # Obtiene el precio del material
        return self.__precio

    def set_precio(self, precio): # Establece el precio del material
        if precio < 0:
            raise ValueError("El precio no puede ser menor a 0")
        else:
            self.__precio = precio
            
    # Muestra la descripcion del material, por polimofismo, será la base para la descripción de los materiales hijos (revistas, libros y periódicos)
    def descripcion(self): 
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Precio: ${self.__precio}")
        print(f"Estado: {'Nuevo' if self.__es_nuevo else 'Usado'}")