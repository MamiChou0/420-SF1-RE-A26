choix = int(input("1) ajouter\n2) retirer\n3) afficher\nChoix? "))

match choix:
    case 1:
        print("Ajout")
    case 2:
        print("Retrait")
    case 3:
        print("Affichage")
    case _:
        print("Choix invalide")

# Équivalent if elif else
if choix == 1:
    print("Ajout (if)")
elif choix == 2:
    print("Retrait (elif)")
elif choix == 3:
    print("Affichage (elif)")
else:
    print("Choix invalide (else)")


lettre = input("Lettre?")

match lettre:
    case "A":
        print("A")
    case "a":
        print("a")
    case _:
        print("pas a ou A")

