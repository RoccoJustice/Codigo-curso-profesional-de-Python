
import time

class FiboIter():

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0 # para llevar la cuenta de las vueltas que estoy dando en mi iterador
        return self

    def __next__(self): 
        if self.counter == 0: # si estoy en el primer elemento de mi iterador
            self.counter += 1
            return self.n1
        elif self.counter == 1: # si estoy en la segunda vuelta de mi iterador
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2 # creo un atributo auxiliar que es igual a la suma de ambos números
            # self.n1 = self.n2 # estas dos línea lo hago si no supiera hacer el swap de abajo; es lo mismo
            # self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux # mediante un swap, asigno el valor de n2 a n1 y el valor de aux a n2; paso un lugar a la derecha dentro de la sucesión. Ahora ni vale n2 y n2 vale aux
            self.counter += 1
            return self.aux

if __name__ == '__main__':
    fibonacci = FiboIter() # instancio el iterador; le doy los valores iniciales de mi iterador
    for element in fibonacci:
        print(element)
        time.sleep(1) # como Python es muy veloz, le pongo un delay de 1 seg con este método que importe al principio

