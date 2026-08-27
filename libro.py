from material import Material # Clase padre para todos los materiales de la biblioteca

class Libro(Material): # Clase hija de la clase Material, representa un libro en la biblioteca
    def __init__(self, titulo, autor, precio, es_nuevo, paginas):
        super().__init__(titulo, autor, precio, es_nuevo)
        if paginas < 0:
            raise ValueError("El numero de paginas no puede ser menor a 0")
        else:
            self.__paginas = paginas
    
    def get_paginas(self): # Obtiene el numero de paginas del libro
        return self.__paginas

    def set_paginas(self, paginas): # Establece el numero de paginas del libro
        if paginas < 0:
            raise ValueError("El numero de paginas no puede ser menor a 0")
        else:
            self.__paginas = paginas

    def descripcion(self): # Muestra la descripcion del libro usando polimorfismo para el llamado de la descripcion de la clase padre Material
        super().descripcion()
        print(f"Paginas: {self.__paginas}")