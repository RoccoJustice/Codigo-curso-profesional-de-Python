import time
"""
def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0
    while True: # ciclo infinito
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux # swaping n1 pasa a tener el valor de n2 y n2 el valor de aux
            counter += 1
            if n2 >= maximo:
                raise StopIteration
            yield aux

if __name__ == '__main__':
    maximo = int(input("Inserta un número: "))
    print(f'Los número de la secuencia de Fibonacci entre 0 y {maximo} son: ')
    fibonacci = fibo_gen() # instancio el generador
    for element in fibonacci:
        print(element)
        time.sleep(0.5) # delay en segudos para ver el resultado de forma lenta
"""

def fibo_gen(max = None):
    n1, n2 = 0, 1
    while not max or max >= n1:
        yield n1
        n1, n2 = n2, n1 + n2
    
if __name__ == '__main__':
    numero = int(input("Inserta un numero: "))
    fibonacci = fibo_gen(numero)
    for element in fibonacci:
        print(element)
        time.sleep(0.5)