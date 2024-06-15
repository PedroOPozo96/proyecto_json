import json
from funciones  import listar_libros, contar_libros, libros_por_fecha, titulos_por_autor, buscar_libros_por_precio

def cargar_datos():
    archivo = 'libros.json'
    with open(archivo, 'r', encoding='utf-8') as fichero:
        datos = json.load(fichero)
    return datos['libros']

def mostrar_menu():
    print("\nMenú de Opciones")
    print("1. Listar los títulos de todos los libros")
    print("2. Contar el número total de libros")
    print("3. Buscar libros por año de publicación")
    print("4. Mostrar títulos de libros por un autor específico")
    print ("5. Buscar libros por el precio")
    print("6. Salir")



def main():

    libros = cargar_datos()
    
    programa_principal = True
    while programa_principal:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\nLista de todos los libros:")
            for titulo in listar_libros(libros):
                print(titulo)

        elif opcion == '2':
            print("\nNúmero total de libros:")
            print(contar_libros(libros))

        elif opcion == '3':
            fecha = input("Introduce el año de publicación: ")
            print(f"\nLibros publicados en {fecha}:")
            for libro in libros_por_fecha(libros, fecha):
                print(libro['nombre'])

        elif opcion == '4':
            autor = input("Introduce el nombre del autor: ")
            print(f"\nTítulos de libros escritos por {autor}:")
            for titulo in titulos_por_autor(libros, autor):
                print(titulo)

        
        elif opcion == '5':
            precio = float(input("Introduce el precio del libro: "))
            print(f"\nLibros con ese precio {precio}:")
            libros_precio = buscar_libros_por_precio(libros, precio)  
            if libros_precio:
                for libro in libros_precio:
                    
                    print(f"Título: {libro['nombre']}")
                    print(f"Autor: {libro['autor']}")
                    print(f"Año de Publicación: {libro['fecha_publicacion']}")
                    print(f"Editorial: {libro['editorial']}")
                    print("-" * 40)


            else:
                print("No está disponible el libro con ese precio")

                
        elif opcion == '6':
                    # Salir
                    programa_principal = False

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
