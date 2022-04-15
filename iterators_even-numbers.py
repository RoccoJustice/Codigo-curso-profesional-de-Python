
class EvenNumbers:

    # Clase que implementa un iterador de todos los números pares, o los números pares hasta un máximo

    def __init__(self, max = None):
        self.max = max # self hace referencia al objeto futuro que voy a crear con esta clase
    
    def __iter__(self): # este método sirve para tener elementos/atributos que voy a necesitar para que mi método funcione
        self.num = 0 # este es el único atributo que necesito, como voy a imprimir todos los números pares, es cada uno de los números de esa iteración y le asigno el primer número par que es 0
        return self # retorno al objeto en sí mismo para poder tenerlo disponible después
    
    def __next__(self): # este método es el que me permite extraer cada uno de los elementos de mi iterador
        if not self.max or self.num <= self.max: # ¿Si no existe self.max (si no se me pasó el número máximo como parámetro) o el número que estoy recorriendo en esta vuelta de mi iterador es menor o igual a self.max, es decir, estoy recorriendo un numero y todavía no llegué al máximo o estoy ya en el máximo
            result = self.num # le asigno el valor de self.num a mi variable porque result va a ser la variable que voy a presentar después en la pantalla
            self.num += 2
            return result 
        else:
            raise StopIteration


