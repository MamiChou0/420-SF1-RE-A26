citation = "Tout le monde a des idées : la preuve, c'est qu'il y en a de mauvaises."

compteur = 0

for lettre in citation:

    match lettre:
        case "a":
            compteur += 1
        case "e":
            compteur += 1
        case "é":
            compteur += 1
        case "i":
            compteur += 1
        case "o":
            compteur += 1
        case "u":
            compteur += 1
        case "y":
            compteur += 1
        case _:
            pass

print(f"Nb voyelles: {compteur}")
