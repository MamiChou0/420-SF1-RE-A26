
# for s'attend à parcourir une liste/séquence

# Dans ce cas-ci, une liste
fruits = ["fraises", "framboises", "bleuets"]

for f in fruits:
    print(f)

# Une séquence de nombre générée par range
for i in range(1, 10):
    print(i)

# Une str est une chaîne de caractères, donc une liste de caractères. La parcourir avec une boucle for va itérer sur les
# caractères
phrase = "J'aime le python!"
for caractere in phrase:
    print(caractere)

# Les tuples sont aussi des séquences
sequence_tuple = (0, 1, 2, 42, 54)
for nbr in sequence_tuple:
    print(nbr)


