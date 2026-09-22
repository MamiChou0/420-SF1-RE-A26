citation = "Tout le monde a des idées : la preuve, c'est qu'il y en a de mauvaises."

voyelles = "aeéiouy"
compteur = 0

for lettre in citation:
    if lettre in voyelles:
        compteur += 1

print(f"Nb voyelles: {compteur}")


# Autre exemple avec "in"

liste_termes = [1, 3, 6, 7, 6, 9, 42]

print(42 in liste_termes)

liste_comp = [i for i in range(0, 100)]

print(liste_comp)