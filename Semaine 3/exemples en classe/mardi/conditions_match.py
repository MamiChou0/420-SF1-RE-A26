choix_menu = input("[A] Ajouter un élément\n[B] Retirer un élément\n[C] Afficher\nChoix: ")

match choix_menu:
    case "A":
        print("Ajout")
    case "B":
        print("Retirer")
    case "C":
        print("Afficher")
    case _:
        print("Choix invalide")

# C'est l'équivalent de faire
if choix_menu == "A":
    print("Ajout if")
elif choix_menu == "B":
    print("Retirer if")
elif choix_menu == "C":
    print("Afficher if")
else:
    print("Choix invalide if")
