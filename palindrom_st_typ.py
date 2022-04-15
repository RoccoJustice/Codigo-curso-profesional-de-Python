
def is_palindrome(string: str) -> bool:
    string = string.lower() # pongo mi string en minúsculas
    string = string.replace(' ', '') # borro los espacios
    return (string == string[::-1])  # Retorna si el string es un palíndromo o no (True or False). [::1] voltea la string al revés

def run():
    print(is_palindrome(1000))
    #print(is_palindrome('Ana'))

if __name__ == '__main__':
    run()
