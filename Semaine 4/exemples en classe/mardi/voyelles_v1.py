citation = "Tout le monde a des idées : la preuve, c'est qu'il y en a de mauvaises."

voyelles = "aeiouyé"

compteur = 0
for lettre in citation:
    if voyelles.find(lettre) != -1:
        compteur += 1

print(f"Nb voyelles: {compteur}")
