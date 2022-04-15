"""
# UNION
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 | my_set2
print(my_set3)
"""
"""
# INTERSECTION
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 & my_set2
print(my_set3)
"""
"""
# DIFERENCE
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 - my_set2 # del set1 , quito todos los elementos que tiene el set2 que se repiten en el set1
print(my_set3)

my_set3 = my_set2 - my_set1 # del set2 , quito todos los elementos que tiene el set1 que se repiten en el set2
print(my_set3)
"""
"""
# SYMMETRIC SIFFERENCE
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 ^ my_set2
print(my_set3)
"""


my_set1 = {1, 2, 3, ("Jose", "Mary", "Carmen", True, 39, 26), False, "Alert"}
my_set2 = {3, 4, 5, ("Carlos", "Pepe", "Mary", True), False, "Alert"}

my_set3 = my_set1 | my_set2 # UNION
print(f'UNION: {my_set3}')

my_set3 = my_set1 & my_set2 # INTERSECTION
print(f'INTERSECTION: {my_set3}')

my_set3 = my_set1 - my_set2 # DIFFERENCE myset1 - myset2
print(f'DIFFERENCE 1-2: {my_set3}')

my_set3 = my_set2 - my_set1 # DIFFERENCE  myset2 - myset1
print(f'DIFFERENCE 2-1: {my_set3}')

my_set3 = my_set1 ^ my_set2 # SYMMETRIC DIFFERENCE
print(f'SYMMETRIC DIFFERENCE: {my_set3}')


