from funciones import (cargar_json, mostrar_menu, lista_libros, contar_libros, libros_por_fecha, libros_por_precio, titulos_por_autor)


#Progrma Principal



def main():
    libros = cargar_json()

    programa_principal = True
    while programa_principal:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")


        if opcion == '1':
            lista_libros(libros)

        elif opcion == '2':
            print("\n Nº de Libros: ")
            print(contar_libros(libros))
        
        elif opcion == '3':
            fecha = input("Indica el año de publicación: ")
            libros_por_fecha(libros, fecha)
        
        elif opcion == '4':
            autor = input("Indica el autor del libro: ")
            titulos_por_autor(libros, autor)


        elif opcion == '5':
            precio = float(input("Indica el precio del libro: "))
            libros_por_precio(libros, precio)

        elif opcion == '6':
            programa_principal = False

        else:
            print("Opción erronea, selecciona una correcta.")


if __name__ == "__main__":
    main()
