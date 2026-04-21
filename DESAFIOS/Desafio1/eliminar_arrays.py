def eliminar_duplicados(array):
    vistos = set()
    resultado = []
    for elemento in array:
        if elemento not in vistos:
            vistos.add(elemento)
            resultado.append(elemento)
    return resultado

# Pruebas
print(eliminar_duplicados([3, 1, 2, 1, 3]))   
print(eliminar_duplicados(["b", "a", "b", "c"]))  
print(eliminar_duplicados([]))                     
print(eliminar_duplicados([7, 7, 7]))              