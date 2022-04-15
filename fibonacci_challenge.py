import time

class FiboIter():
    
    def __init__(self, maximum):
        self.maximum = maximum
        pass

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        elif self.n2 < maximum:
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            if self.n2 >= maximum:
                raise StopIteration
            return self.aux

if __name__ == '__main__':
    maximum = int(input("Inserta el número máximo para secuencia de FIbonacci: "))
    print(f'Estos son todos los número que hay entre 0 y {maximum} de la secuencia de Fibonacci:')
    fibonacci = FiboIter(maximum)
    for element in fibonacci:
        print(element)
        time.sleep(0.05)

