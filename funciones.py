   


# 1. Lista de los títulos de los libros.

def listar_libros(libros):
    titulos = [libro['nombre'] for libro in libros]
    return titulos

#2. Contar el número total de libros.

def contar_libros(libros):
    return len(libros)


#3.Buscar libro por fecha de publicación

def libros_por_fecha(libros, fecha):
     libros_fecha = [libro for libro in libros if libro['fecha_publicacion'] == str(fecha)]
     return libros_fecha


#4. Buscar el nombre del autor y que te devuelva el libro.

def titulos_por_autor(libros, autor):
    titulos_autor = [libro['nombre'] for libro in libros if libro['autor'] == autor]
    return titulos_autor




#5. Buscar libros por Precio.

def buscar_libros_por_precio(libros, precio):  
    libros_precio = [libro for libro in libros if libro['precio'] == precio]
    return libros_precio





