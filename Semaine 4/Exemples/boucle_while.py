
# On demande à l'utilisateur d'entrer un nombre, on convertit la str en int
nombre = int(input("Entrez le nombre pour la table de multiplication: "))
# Affiche l'entête
print("Table de multiplication de ", nombre)
print("**" * 5)
# initialise le compteur
i = 1
# Tant que i est plus petit que 11, le bloc d'instructions de la boucle sera exécuté
while i < 11:
    print(i, " * ", nombre, " = ", i * nombre)
    # On incrémente notre compteur
    i += 1  # même chose que i = i + 1

print("**" * 5)


