import random as r

nombre_a_deviner = r.randint(0, 10)

choix = int(input("Devinez le nombre entre 0 et 10: "))

if choix == nombre_a_deviner:
    print("Vous avez gagné!")
else:
    print("Mauvais choix!")
