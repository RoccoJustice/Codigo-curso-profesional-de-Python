"""
def my_gen():

    print('Hello world!')
    n = 0
    yield n # es exactamente lo mismo que return pero detiene la función en lugar de terminarla, para que cuando se vuelva a llamar a la función, siga desde donde se llamó al último yield. Por eso se dice que el generador guarda el estado.

    print('Hello heaven!')
    n = 1
    yield n

    print('Hello hell!')
    n = 2
    yield n


a = my_gen() # en "a" se va a guardar el resultado de ejecutar la función "my_gen"
print(next(a)) # Hello world!, next me lleva hasta el yield más próximo
print(next(a)) # Hello heaven!, next me lleva hasta el yield más próximo
print(next(a)) # Hello hell!, next me lleva hasta el yield más próximo
print(next(a)) # Se eleva el error StopIteration
"""

my_list = [0, 1, 4, 7, 9, 10]

my_second_list = [x ** 2 for x in my_list] # List comprehension; saca todos los elementos
my_second_gen = (x ** 2 for x in my_list) # Generator expression; saca un elemento a la vez

print(my_second_list)
print(my_second_gen)
for i in my_second_gen:
    print(i)