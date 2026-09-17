# Citation de Dijkstra
citation = ("La question de savoir si les ordinateurs peuvent penser est comme la question de savoir si les "
            "sous-marins peuvent nager.")

nb_voyelles = 0
for lettre in citation:

    if lettre == "a" or lettre == "e" or lettre == "i" or lettre == "o" or lettre == "u" or lettre == "y":
        nb_voyelles += 1
print(f"Nb voyelles: {nb_voyelles}")

compte = 0

compte += citation.count("a")
compte += citation.count("e")
compte += citation.count("i")
compte += citation.count("o")
compte += citation.count("u")
compte += citation.count("y")

print(f"Nb voyelles: {compte}")

compte_voyelles = 0
liste_voyelles = ["a", "e", "i", "o", "u", "y"]

for lettre in citation:
    if lettre in liste_voyelles:
        compte_voyelles += 1
print(f"Nb voyelles: {compte_voyelles}")


nb_voy = 0

for lettre in citation:
    if lettre in "aeiouy":
        nb_voy += 1
print(f"Nb voyelles: {nb_voy}")





