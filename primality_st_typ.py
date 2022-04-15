    
def primalidad(num = int) -> bool:
    primo = True
    while primo:
        for i in range(2, num):
            if num % i == 0:
                primo = False
        break
    return "es primo" #debe regresar un bool pero le pongo esto para probar mypy en la consola
    # return primo

def run():
    print(primalidad(float((input(("Ingresa un numero: ")))))) # le estoy tratando de pasar un float cuando desde la función defino que le debo de pasar un entero

if __name__ == '__main__':
    run()

# código pra probar con mypy: mypy primalidad_tipado_est.py --check-untyped-defs