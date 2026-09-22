citation = "Tout le monde a des idées : la preuve, c'est qu'il y en a de mauvaises."

compteur = 0

compteur += citation.count("a")
compteur += citation.count("e")
compteur += citation.count("é")
compteur += citation.count("i")
compteur += citation.count("o")
compteur += citation.count("u")
compteur += citation.count("y")

print(f"Nb voyelles: {compteur}")
