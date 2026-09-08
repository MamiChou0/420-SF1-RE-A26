# Pour utiliser un ' dans un str déclarée avec ''
martine = 'Martine s\'en va à l\'étable'

# De même
citation = "Socrate: \"Je sais que je ne sais rien!\""

# Autres caractères d'échappement
# tabulation
tabulation = "Nom:\tPier Luc"
print(tabulation)

# nouvelle ligne
texte_avec_ligne = "Ceci est une ligne\nCeci est une autre ligne"
print(texte_avec_ligne)

# pour utiliser le \ dans un texte
barre_oblique = "Ceci est une barre oblique: \\"
print(barre_oblique)

# On peut utiliser \ pour faire un texte sur plusieurs lignes
texte_multi = "Texte déclaré sur plusieurs lignes; ceci n'affiche pas de nouvelle ligne à la console, mais permet de \
déclarer un texte sur plusieurs lignes"

# On peut aussi englober plusieurs str dans des parenthèses pour déclarer sur plusieurs lignes (défaut de PyCharm)
texte_multi2 = ("Texte déclaré sur plusieurs "
                "lignes")

# Utilisation de unicode (utf-8)
str_avec_unicode = "un caractère unicode: \u2661"
print(str_avec_unicode)

# Si le code unicode est de plus de 4 caractères, on utilise le \U et on complète la valeur pour avoir 8 caractères en
# ajoutant des 0 en préfixe
emoji = "\U0001F9D0"
print(emoji)

# de même façon
coeur = "\U00002661"
print(coeur)

# Ex: Oméga
print("\u038F")
