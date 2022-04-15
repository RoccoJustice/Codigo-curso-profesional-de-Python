"""
def decorador(func):
    def envoltura():
        print("Este es el decorador de mi función original :/") # lo que le quiero agregar a mi función original
        func()
    return envoltura

def saludo():
    print("!Hola¡")

saludo()
greeting = decorador(saludo) # el parámetro es la función que quiero decorar, que a su vez la asigno a una variable
# saludo = decorador(saludo) -> es lo mismo que arriba pero con otro nombre de variable
greeting()
# saludo() -> es lo mismo que arriba pero para el otro nombre de variable
"""
"""
def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

print(mensaje('Cesar'))
"""
"""
from datetime import datetime

def exec_time(func): # tiempo que tarda en ejecutarse
    def wrapper(*args, **kwargs): # lo que le estoy diciendo a wrapper es que no importa la cantidad de argumentos posicionales, la función los va a recibir. Tampoco le va a importar la cantidad de argumentos nombrados que se le envíen. Así le pasemos "n" argumentos posicionales y "m" argumentos nombrados, el decorador se va a ejecutar si o si.
        initial_time = datetime.now() # devuelve la fecha y hora en la que se ejecuta esta línea de código
        func(*args, **kwargs) # lo que le estoy diciendo a func es que no importa la cantidad de argumentos posicionales, la función los va a recibir. Tampoco le va a importar la cantidad de argumentos nombrados que se le envíen
        final_time = datetime.now()
        time_elapsed = final_time - initial_time # devuelve la fecha y hora en la que se ejecuta esta línea de código
        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
    return wrapper

@exec_time
def random_func():
    for _ in range(1, 10000000): # Pongo un "_" porque no me interesa la variable de este ciclo para este ejercicio en específico
        pass

@exec_time
def sum(a: int, b: int) -> int:
    return a+b

@exec_time
def saludo(name):
    print(f'Hola {name}')

random_func()
sum(5, 5)
saludo(input("Inserta tu nombre: "))
"""

def data_type(func):
    def wrapper(*args, **kwargs):
        if type(*args, **kwargs) is str:
            print(f'{func(*args, **kwargs)}, es un dato del tipo string')
        elif type(*args, **kwargs) is int:
            print(f'{func(*args, **kwargs)}, es un dato del tipo entero')
        elif type(*args, **kwargs) is bool:
            print(f'{func(*args, **kwargs)}, es un dato del tipo booleano')
        
    return wrapper

@data_type
def data(a):
    return a
    
data(input("Inserta una palabra: "))
data(int(input("Inserta un numero entero: ")))
data(bool(input("¿True or False?: ")))
