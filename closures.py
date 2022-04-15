"""
def make_multiplier(x):
	def multiplier(n): # nested function
		return x*n # referencia a una variable de un scope superior
	return multiplier # retorna la funcion anidada

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3)) # 30
print(times4(5)) # 20
print(times10(times4(2))) # 80
"""
"""
# Hola 3 -> HolaHolaHola
#Facundo 2 -> FacundoFacundo

def make_repeater_of(n):
	def repeater(string):
		assert type(string) == str, "Solo puede utilizar cadenas"
		return string * n
	return repeater

def run():
	# repeat_5 = make_repeater_of(5)
	repeat_5 = make_repeater_of(int(input("Escribe un número: ")))
	# print(repeat_5("Hola"))
	print(repeat_5(input("Escribe una frase: ")))

if __name__ == '__main__':
	run()
"""


def make_division_by(n):
	# This closure returns a function that returns the division of an x number by n
	def division_by(x):
		return x / n
	return division_by

def run():
	division_by_n = make_division_by(float(input("Inserta el denominador: ")))
	print(division_by_n(float(input("Inserta el numerador: "))))

if __name__ == '__main__':
	run()