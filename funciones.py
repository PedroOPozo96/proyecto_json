import json

#Datos del Json

def cargar_json():
    archivo = 'libros.json'
    with open(archivo, 'r', encoding = 'utf-8') as fichero:
        datos = json.load(fichero)
    return datos['libros']


#Menú


def mostrar_menu():
    print("\n Menú: ")
    print("1. Lista de los libros.")
    print("2. Contar el número total de libros. ")
    print("3. Libros por año de publicación.")
    print("4. Libros por autor.")
    print("5. Libros por precio.")
    print("6. Salir del programa.")





#1. Lista de los libros.


def lista_libros(libros):
    libros_por_pagina = 10
    total_libros = len(libros)
    paginas = (total_libros + libros_por_pagina - 1) // libros_por_pagina
    pagina_actual = 0
    continuar = True

    
    while continuar and pagina_actual < paginas:
        print(f"\nPágina {pagina_actual + 1} de {paginas}")
        inicio = pagina_actual * libros_por_pagina
        fin = inicio + libros_por_pagina

        for libro in libros[inicio:fin]:
              print(f"• \033[1m{libro['nombre']}\033[0m")
              print("")

        if pagina_actual + 1 < paginas:
            opcion = input("Indica 's' para siguiente página o 'm' para volver al menú: ")
            if opcion.lower() == 's':
                    pagina_actual += 1
            elif opcion.lower() =='m':
                    continuar = False
            else: 
                    print ('Opción no válida.')
        else:
             input("Presione 'm' para volver")
             continuar = False

                

#2. Contar el número de libros

def contar_libros(libros):
    return len(libros)


#3. Buscar libro por fecha de publicación

def libros_por_fecha(libros, fecha):
    libros_fecha = [libro for libro in libros if libro['fecha_publicacion'] == str(fecha)]
    print(f"\n Libros publicados en {fecha}: ")
    for libro in libros_fecha:
        print(f"• \033[1m{libro['nombre']}\033[0m")
        print("")





#4. Buscar libro por autor

def titulos_por_autor(libros, autor):
    libros_autor = [libro for libro in libros if libro['autor'] == autor]
    print(f"\nTítulos de libros escritos por {autor}:")
    for libro in libros_autor:
        print(f"• \033[1m{libro['nombre']}\033[0m")
        print("") 




#5. Libros por precio

def libros_por_precio(libros, precio):
    libros_precio = [libro for libro in libros if libro['precio'] == precio]
    if libros_precio:
                for libro in libros_precio:
                    
                    print(f"Título: \033[1m{libro['nombre']}\033[0m")
                    print(f"Autor: \033[1m{libro['autor']}\033[0m")
                    print(f"Año de Publicación: \033[1m{libro['fecha_publicacion']}\033[0m")
                    print(f"Editorial: \033[1m{libro['editorial']}\033[0m")
                    print("-" * 40)

    else:
        print("No está disponible el libro con ese precio")