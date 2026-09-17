import random

a_deviner = random.randint(1, 100)
essais_max = 10

for essais in range(1, essais_max + 1):
    choix = int(input(f"Essai {essais}: Devinez un nombre de 1 à 100"))

    if choix == a_deviner:
        print("Bravo! Vous avez gagné! \U0001F387")
        # exit(code) termine le programme avec le code en paramètre
        exit(0)
    elif a_deviner < choix:
        print("La réponse est plus petite")
    else:
        print("La réponse est plus grande")
print("Nombre d'essais maximum atteint. Meilleur chance la prochaine fois \U0001F62D")


