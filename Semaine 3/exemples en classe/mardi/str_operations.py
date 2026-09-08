# Pour la longueur d'une str (nb de caractères), on utilise la fonction built-in len()
ma_str = "Ceci est ma str"
print(len(ma_str))

# À noter que les caractères échappés compte dans la longueur
str2 = "Nom\tDucharme\nfin"
print(len(str2))

# On peut additionner (concatener) les str entre elles
str3 = "Ceci est une nouvelle str: " + "on additionne une autre str"
print(str3)

# On peut aussi les caractères dans une chaîne
nouvelle_chaine = "->" * 5 + "texte" + ">" * 6
print(nouvelle_chaine)
print(nouvelle_chaine*7)

# On peut mettre une str en majuscule ou minuscule
citation3 = "Le courage n’est pas l’absence de peur, mais la capacité de vaincre ce qui fait peur."
citation_maj = citation3.upper()
print(citation_maj)
citation_min = citation3.lower()
print(citation_min)

# count(sous-chaîne) permet de compter le nombre de sous-chaînes dans la str
citation4 = ("Il y a deux manières de vivre : l'une en faisant comme si rien n'était un miracle, l'autre en considérant"
             " tout comme un miracle.")
print(citation4.count("miracle"))
# index donne l'index où se trouve la sous-chaîne
print(citation4.index("miracle"))
# count(str, debut, fin) permet de spécifier les bornes de recherches
print(citation4.count("miracle", 80))
# de même façon, index(str, debut, fin)
print(citation4.index("miracle", 80))
# find() agit comme index, sauf que retourne -1 si la chaîne est non-trouvée. Index donne une erreur si la chaîne est
# non-trouvée
print(citation4.find("miracle"))
print(citation4.find("patate"))
print(citation4.index("patate"))

# Pour toutes les méthodes sur les str
# https://docs.python.org/fr/3.14/library/stdtypes.html#string-methods



