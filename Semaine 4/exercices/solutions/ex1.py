hauteur = int(input("Entrer la hauteur du triangle: "))

# Boucle pour les lignes de la première moitié du triangle
for ligne in range(hauteur):
    # on va générer une séquence qui va permettre d'afficher le même nombre d'étoiles que la ligne
    for etoile in range(ligne):
        # on affiche une étoile à chaque itération en s'assurant que le print n'ajoute pas de fin de ligne
        print("* ", end="")
    # Comme on a supprimé les fins de ligne, il faut faire un print() standard pour ajouter un \n
    print()

# Boucle pour la deuxième moitié du triangle, on commence à hauteur et on réduit de 1 à chaque fois
# donc de hauteur à 1 inclus
for ligne in range(hauteur, 0, -1):
    # on va générer une séquence qui va permettre d'afficher le même nombre d'étoiles que la ligne
    for etoile in range(ligne):
        print("* ", end="")
    # Comme on a supprimé les fins de ligne, il faut faire un print() standard pour ajouter un \n
    print()

