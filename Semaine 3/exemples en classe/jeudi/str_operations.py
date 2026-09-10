# len() retourne une longueur de séquence (ex: string)
bonjour = "Bonjour, les amis!"
print(len(bonjour))

# pour retourner une sous-chaîne (splicing ou slicing), on utilise l'opérateur d'indexation s[debut:fin_non_inclus]
print(bonjour[0:5])
print(bonjour[1:7])
# Si début et fin sont égaux, retourne une chaîne vide
print(bonjour[1:1])
print(bonjour[21:26])

# Si on omet le début, ce sera le début de la chaîne par défaut
print(bonjour[:15])
# Si on omet la fin ou on excède la limite, ça va jusqu'à la fin
print(bonjour[5:])
print(bonjour[5:400])
# [:] retourne la str en entier
print(bonjour[:])

# On peut concatener des str en utilisant +
une_chaine = "première chaîne"
une_autre_chaine = "deuxième chaîne"
print(une_chaine + une_autre_chaine)

# On peut multiplier les chaînes
print("----" * 5 + "->" * 7)

# Pour toutes les fonctions sur les str: https://docs.python.org/fr/3.14/library/stdtypes.html#string-methods

