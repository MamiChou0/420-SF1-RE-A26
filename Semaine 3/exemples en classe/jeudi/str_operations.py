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

# on peut faire du formattage et de la substitution avec format
salutations = "Bonjour {}"
print(salutations.format("Pier Luc"))
print(salutations.format("Mustapha"))
double_salutations = "Allo {} et {}"
print(double_salutations.format("Pier Luc", "Mustapha"))

# On peut aussi utiliser les format strings (fstrings) en préfixant la str avec f
legume1 = "patate"
legume2 = "carotte"

print(f"Dans mon panier, j'ai une {legume1} et une {legume2}")
# on peut utiliser format ou fstrings pour formatter des nombres
nombre = 42.87654321
print(f"{nombre:.5g}")
print(f"{nombre:.6f}")

ma_super_str = "ceci est ma super str. Célébrations!"
print(ma_super_str.capitalize())

print(ma_super_str.upper())
print(ma_super_str.lower())

# count(sous-chaîne) permet de compter le nombre de sous-chaînes dans la str
str_repete = "Fais de ta vie un rêve et d'un rêve une réalité."
print(str_repete.count("rêve"))
# On peut commencer la recherche à partir d'un index et la terminé à une limite
print(str_repete.count("rêve", 20))

# On peut trouver l'index d'une sous-chaîne avec find() ou index()
print(str_repete.find("rêve"))
print(str_repete.find("patate"))
print(str_repete.index("rêve"))
# print(str_repete.index("patate"))

print(str_repete.replace("rêve", "enfer"))

# strip, lstrip, rstrip enlève les caractères au début et à la fin
str_strip = "      Ceci est mon texte!     "
print(str_strip.strip())
print(str_strip.lstrip())
print(str_strip.rstrip())
autre_str = "->->Départ->->"
print(autre_str.strip("->"))














