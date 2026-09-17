import random

a_deviner = random.randint(1, 10)

while True:
    choix = int(input("Entrez un nombre de 1 à 10: "))

    if choix == a_deviner:
        print("Vous avez gagné!")
        break
    print("Mauvais choix!")
