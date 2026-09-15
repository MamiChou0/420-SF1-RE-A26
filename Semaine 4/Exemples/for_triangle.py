# boucle niveau 1
for i in range(1, 6):
    barre = ""
    # à chaque itération de la boucle de niveau 1, le nombre d'itérations de la boucle de niveau 2 sera incrémenté de 1
    for j in range(1, i+1):
        barre += "#"
    print(barre)
