import math


# Arguments avec défaut, deviennent optionnels
def hypothenuse(a=3, b=4):
    print(f"c = {math.sqrt(a**2 + b**2)}")


hypothenuse(5)  # a=5, b=4
hypothenuse()  # a=3, b=4

hypothenuse(b=7)  # a=3, b=7


# exemple de la table de multiplication
def table_de_multiplication(base=5, initial=1, final=10):
    n = initial
    while n <= final:
        print(f"{n} * {base} = {n * base}")
        n += 1


# Va utiliser toutes les valeurs par défaut
table_de_multiplication()
# Si on met 1 argument, il sera assigné au premier paramètre, les autres utiliseront le défaut
table_de_multiplication(6)
# Si je veux en spécifier un en particulier, celui-là sera remplacé, les autres utiliseront les valeurs par défaut
table_de_multiplication(final=20)


