# [1, 1, 2, 2, 4] -> [1, 2, 4]
"""
def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    run()
"""

def run():
    random_list = []
    more = True
    while more:
        element = input("Inserta un elemento a la lista: ")
        random_list.append(element.lower())
        answer = input("¿Quieres seguir agregando elementos (Y/N)?: ")
        if answer.lower() == "n":
            more = False
    
    my_set = set(random_list)
    new_list = list(my_set)
    print(new_list)

if __name__ == '__main__':
    run()