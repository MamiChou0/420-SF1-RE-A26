# Il y a plusieurs façons d'afficher le tout, soit en faisant une str contenant tous les caractères UTF-8 ou
# en utilisant la multiplication.
print("\u2659 \u2659 \u2659 \u2659 \u2659 \u2659 \u2659 \u2659")
print("\u2656 \u2658 \u2657 \u2655 \u2654 \u2657 \u2658 \u2656")

# Autre version plus fancy
# On multiplie le nombre de pions par 8 avec l'espace
ligne_pions = "\u2659 " * 8
# On enlève l'espace supplémentaire à la fin
ligne_pions = ligne_pions.strip()
print(ligne_pions)
# On définit les premières pièces
tour_chevalier_fou = "\u2656 \u2658 \u2657"
# On affiche les premières pièces, ensuite la reine et le roi et on affiche la chaîne inverse des premières pièces.
print(tour_chevalier_fou, "\u2655 \u2654", tour_chevalier_fou[::-1])




