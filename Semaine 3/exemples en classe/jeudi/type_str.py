# Déclaration
ma_str = "un texte"
ma_str2 = 'un autre texte'

# Caractères d'échappements
# pour échapper un guillemet
une_citation = "Descartes a dit: \"Je pense, donc je suis.\""
print(une_citation)

# échapper un apostrophe
str_apo = 'Martine s\'en va à l\'étable'
str_guil = "Martine s'en va à l'étable"

# Pour une nouvelle ligne
multi = "Ceci est une ligne\nCeci est une autre ligne"
print(multi)

# tabulation
tab = "Nom:\tDucharme"
print(tab)

# Sur plusieurs lignes
long_texte = "Ceci est un long texte qui ne pourra pas être déclaré sur une seule ligne. Plusieurs lignes seront \
nécessaires pour éviter de dépasser le nombre de caractère d'un ligne"
# Autre façon
autre_long_texte = ("Alice's Adventures in Wonderland by Lewis Carroll is a children's novel published in 1865. When a"
                    " curious girl named Alice spots a White Rabbit with a pocket watch, she tumbles down a rabbit hole"
                    " into an extraordinary fantasy world filled with peculiar anthropomorphic creatures")

# échaper un \
texte_avec_backslash = "Chemin c:\\temp"
print(texte_avec_backslash)

# unicode
print("pi: \u03C0")
# Si le caractère unicode à une valeur à plus de 4 "hexadécimales", on utilise \U et on préfixe
# pour avoir 8 "hexadécimales"
print("pouce: \U0001F44D")





