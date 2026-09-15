# on commence à 1 et on utilise un pas de 2 pour incrémenter, on obtient la séquence 1, 3, 5, 7 ...
for i in range(1, 101, 2):
    # Si c'est une mutiple de 7, on continue à la prochaine itération
    if i % 7 == 0:
        continue
    # On imprime les autres nombres avec une fin de ligne vide
    print(str(i) + " ", end="")
