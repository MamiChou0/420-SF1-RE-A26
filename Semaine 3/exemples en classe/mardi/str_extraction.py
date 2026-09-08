# Pour faire l'extaction (splicing), on utilise l'opérateur d'indexation [:]
# [début inclus : fin non incluse]
drole = "C'est drôle!"
print(len(drole))
print(drole[0:5])

# Si on omet le début, il va partir du début... si on omet la fin, il ira jusqu'à la fin
print(drole[:5])
print(drole[0:])
print(drole[:])

# De même façon, on peut utiliser n'importe quel indice pourvu qu'elle soit dans les limites de la chaîne
print(drole[2:10])

# Si début == fin, on obtient une chaîne vide
print(drole[4:4])

# Si début > len()-1, on obtient une chaîne vide
print(drole[42:])

# Si fin > len()-1, l'extraction se fera jusqu'à la fin
print(drole[3:42])

