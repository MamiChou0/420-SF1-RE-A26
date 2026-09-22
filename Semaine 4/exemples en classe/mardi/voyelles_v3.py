citation = "Tout le monde a des idées : la preuve, c'est qu'il y en a de mauvaises."

compteur = 0

for lettre in citation:
    if (lettre == "a" or lettre == "e" or lettre == "é" or lettre == "i" or lettre == "u" or lettre == "y"
            or lettre == "o"):
        compteur += 1

print(f"Nb voyelles: {compteur}")
