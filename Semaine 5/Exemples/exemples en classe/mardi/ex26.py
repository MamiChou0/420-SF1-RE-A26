def saisir_nombres(valider_zero=False):
    nombre1 = int(input("Veuillez saisir le premier nombre: "))
    while True:
        nombre2 = int(input("Veuillez saisir le deuxième nombre: "))
        if valider_zero and nombre2 == 0:
            print("Zéro invalide comme nombre, entrez un autre nombre")
            continue
        break
    return nombre1, nombre2


while True:

    choix = int(input("Veuillez choisir une option:\n\t[1] Addition\n\t[2] Soustraction\n\t[3] Mutliplication"
                "\n\t[4] Division\n\t[5] Exponentiation\nChoix? "))

    match choix:

        case 1:
            nb1, nb2 = saisir_nombres()
            print(f"L'addition de {nb1} et {nb2} donne {nb1+nb2}")
        case 2:
            nb1, nb2 = saisir_nombres()
            print(f"La soustraction de {nb1} et {nb2} donne {nb1-nb2}")
        case 3:
            nb1, nb2 = saisir_nombres()
            print(f"La multiplication de {nb1} et {nb2} donne {nb1*nb2}")
        case 4:
            nb1, nb2 = saisir_nombres(True)
            print(f"La division de {nb1} par {nb2} donne {nb1 / nb2}")
        case 5:
            nb1, nb2 = saisir_nombres()
            print(f"{nb1} puissance {nb2} donne {nb1**nb2}")
        case _:
            print("choix invalide")
