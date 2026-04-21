def encontrar_maximo(array):
    if len(array) == 0:
        return "El array está vacío"
    
    maximo = array[0]
    for elemento in array:
        if elemento > maximo:
            maximo = elemento
    return maximo


def encontrar_minimo(array):
    if len(array) == 0:
        return "El array está vacío"
    
    minimo = array[0]
    for elemento in array:
        if elemento < minimo:
            minimo = elemento
    return minimo


def longitud_cadena(cadena):
    contador = 0
    for _ in cadena:  # recorre cada carácter
        contador += 1
    return contador


# Pruebas máximo y mínimo
numeros = [3, 7, 1, 9, 4, 6, 2]
print(encontrar_maximo(numeros))         
print(encontrar_minimo(numeros))         
print(encontrar_maximo([]))              
print(encontrar_minimo([-5, -1, -8, -3]))

# Pruebas longitud
print(longitud_cadena("hola"))           
print(longitud_cadena("python"))         
print(longitud_cadena(""))               
print(longitud_cadena("hola mundo"))     
print(longitud_cadena("12345"))          