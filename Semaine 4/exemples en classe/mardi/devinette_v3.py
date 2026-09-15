import random

nombre_a_deviner = random.randint(0, 10)
nombre_max_essais = 5
essai_courant = 1

while essai_courant <= nombre_max_essais:
    choix = int(input(f"Essai {essai_courant} Devinez un nombre de 0 et 10: "))

    if choix == nombre_a_deviner:
        print("Vous avez gagné!")
        break
    print("Mauvais choix!")
    essai_courant += 1
print("Nombre d'essais maximum atteint! Meilleure chance la prochaine fois!")