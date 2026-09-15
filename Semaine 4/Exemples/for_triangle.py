# boucle niveau 1
# La première boucle représente la ligne
for i in range(1, 6):
    barre = ""
    # à chaque itération de la boucle de niveau 1, le nombre d'itérations de la boucle de niveau 2 sera incrémenté de 1
    # Cette boucle représente le nombre de fois que les symboles seront affichés sur une ligne
    for j in range(1, i+1):
        barre += "#"
    print(barre)
