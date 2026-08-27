# Profesor Eric Railef Mansilla
# Estudiante: Luis Contreras
from libro import Libro # Clase que representa un libro en la biblioteca
from revista import Revista # Clase que representa una revista en la biblioteca
from periodico import Periodico # Clase que representa un periodico en la biblioteca
from biblioteca import Biblioteca # Clase que representa la biblioteca y contiene los materiales

def main():
    biblioteca = Biblioteca() # Crea una instancia de la clase Biblioteca

    libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 15999, True, 96) # Crea una instancia de la clase Libro
    revista1 = Revista("National Geographic", "Varios autores", 25999, True, 3) # Crea una instancia de la clase Revista
    periodico1 = Periodico("El Mercurio", "Varios autores", 1500, False, "28-08-2026") # Crea una instancia de la clase Periodico

    biblioteca.agregar_material(libro1) # Agrega el libro a la biblioteca
    biblioteca.agregar_material(revista1) # Agrega la revista a la biblioteca
    biblioteca.agregar_material(periodico1) # Agrega el periodico a la biblioteca

    print("\nCatálogo de materiales en la biblioteca:")
    print("----------------------------------------")
    biblioteca.mostrar_catalogo() # Muestra el catalogo de materiales en la biblioteca


if __name__ == "__main__":
    main()