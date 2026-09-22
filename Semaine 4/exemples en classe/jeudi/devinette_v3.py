import random

a_deviner = random.randint(1, 10)
essais_restants = 5

while essais_restants > 0:
    choix = int(input("Devinez un nb de 1 à 10: "))

    if choix == a_deviner:
        print("Vous avez gagné!")
        break
    print("Mauvais choix!")
    essais_restants -= 1

print("Plus d'essais! Meilleure chance la prochaine fois")

