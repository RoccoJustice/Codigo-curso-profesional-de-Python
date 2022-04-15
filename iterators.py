"""
# Creando un iterador
my_list = [1, 2, 3, 4, 5] # Esta lista por sí misma yo no puedo recorrerla en un ciclo for. Es decir, puedo hacerlo dentro de Pytho; crear un ciclo for que recorra cada uno de los elementos. Pero internamente el lenguaje no puede hacerlo.
my_iter = iter(my_list) # Esto es lo que hace el lenguaje internamente cuando itero sobre esta lista. Iter convierte a esta estructura de datos en un iterador. Es decir, todos los iterables pueden convertirse en iteradores. Una vez que yo tengo el iterador, puedo acceder a cada uno de los iterables del cual partió. 

# Iterando un iterador
print(next(my_iter)) # Con next acceso al siguiente elemento del iterador. Imprime 1
print(next(my_iter)) # Imprime 2
print(next(my_iter)) # Imprime 3
print(next(my_iter)) # Imprime 4
print(next(my_iter)) # Imprime 5
# print(next(my_iter)) # Aquí me marcaría error "StopIteration" porque ya me dió todos los valores dentro de mi iterable original.
# Cuando no quedan datos, la excepción StopIteration es elevada.
"""
"""
# Esta es una solución simple pero no es la más práctica
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break
"""



