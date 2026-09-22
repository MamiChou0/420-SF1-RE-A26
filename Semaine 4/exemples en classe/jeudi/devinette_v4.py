import random

a_deviner = random.randint(1, 100)
essais_max = 10
essais_courant = 1

while essais_courant <= essais_max:

    choix = int(input(f"Essai {essais_courant}: Devinez un nombre de 1 à 100: "))

    if choix == a_deviner:
        print("Bravo! Vous avez gagné! \U0001F389")
        break
    elif choix > a_deviner:
        print("La réponse est plus petite")
    else:
        print("La réponse est plus grande")

    essais_courant += 1

    if essais_courant > essais_max:
        print("Plus d'essais, meilleure chance la prochaine fois!")





