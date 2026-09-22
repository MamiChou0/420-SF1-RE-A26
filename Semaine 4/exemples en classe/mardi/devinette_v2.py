import random

nombre_a_deviner = random.randint(0, 10)

while True:
    choix = int(input("Devinez un nombre entre 0 et 10: "))
    if nombre_a_deviner == choix:
        print("Vous avez gagné!")
        break
    else:
        print("Mauvais choix!")
