citation = "Tout le monde a des idées : la preuve, c'est qu'il y en a de mauvaises."

compteur = 0

for lettre in citation:
    if lettre == "a":
        compteur += 1
    elif lettre == "e":
        compteur += 1
    elif lettre == "é":
        compteur += 1
    elif lettre == "i":
        compteur += 1
    elif lettre == "o":
        compteur += 1
    elif lettre == "u":
        compteur += 1
    elif lettre == "y":
        compteur += 1
    else:
        pass

print(f"Nb voyelles: {compteur}")
