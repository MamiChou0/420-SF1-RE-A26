import random

a_deviner = random.randint(1, 10)

choix = int(input("Entrez un nombre de 1 à 10: "))

if choix == a_deviner:
    print("Bravo! Vous avez gagné!")
else:
    print("Mauvais choix!")

