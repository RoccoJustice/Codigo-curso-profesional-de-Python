"""
my_set = {3, 4, 5}
print("my_set = ", my_set)

my_set2 = {"Hola", 23.3, False, True}
print("my_set2 = ", my_set2)

my_set3 = {3, 3, 2}
print("my_set3 = ", my_set3)

my_set4 = {[1, 2, 3], 4} # no es un set ya que contiene una lista
print("my_set4 = ", my_set4)
"""
"""
empty_set = {} # si declaro un set vacío de esta manera, me dirá que es un diccionario
print(type(empty_set))

empty_set = set() # utilizo la función built in set() para poder declarar un set vacío
print(type(empty_set))
"""
"""
# castear listas y tuplas en sets:
my_list = [1, 1, 2, 3, 4, 4, 5]
my_set = set(my_list) # va a quitar los elementos repetidos
print(my_set)

my_tuple = ("hola", "hola", "hola", 1) 
my_set2 = set(my_tuple) # va a quitar los elementos repetidos
print(my_set2)
"""
"""
# añadir elementos a mi set
my_set = {1, 2, 3}
print(my_set)

my_set.add(4) # añade el elemento 4
print(my_set)

my_set.update([1, 2, 5]) # añade cada elemento de la lista excepto los repetidos
print(my_set)

my_set.update((1, 7, 2), {6, 8}) # añade cada elemento de mi tupla y de mi set excepto los repetidos
print(my_set)
"""
"""
# borrar elementos de mi set
my_set = {1, 2, 3, 4, 5, 6 ,7}
print(my_set)

my_set.discard(1) # borra un elemento existente
print(my_set)

my_set.remove(2) # borra un elemento existente
print(my_set)

my_set.discard(10) # borra un elemento existente
print(my_set)

my_set.remove(12) # borra un elemento existente
print(my_set)
"""

# borrar un elementos de mi set
my_set = {1, 2, 3, 4, 5, 6 ,7}
print(my_set)

my_set.pop() # borra un elemnto aleatorio
print(my_set)

my_set.clear() # limpia el set
print(my_set)