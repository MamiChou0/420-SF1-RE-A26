precedent = 0
courant = 1

# On affiche le premier terme, remplace la fin de ligne par un espace
print(precedent, end=" ")
# Tant que la valeur du terme courant est inférieur à 150
while courant < 150:
    # affiche la valeur courante, remplace la fin de ligne par un espace
    print(courant, end=" ")

    # On calcule les nouvelles valeurs des termes. Le courant devient le précédent et le nouveau courant est
    # la somme de lui-même et l'ancien précédent. En utilisant l'affectation multiple, on peut le faire en une ligne.
    precedent, courant = courant, courant + precedent
