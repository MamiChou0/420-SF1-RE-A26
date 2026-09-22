
# nbr_str = input("Nombre épiceries: ")
# nombre_epiceries = int(nbr_str)
# # Boucle niveau 1
# for i in range(1, nombre_epiceries + 1):
#     total = 0.0
#     # boucle niveau 2
#     for j in range(1, 4):
#         montant = float(input(f"Entrer le montant pour épicerie {i} pour le mois {j}"))
#         total += montant
#     print(f"Total pour épicerie {i}: {total}")


nbr_str = input("Nombre épiceries: ")
nombre_epiceries = int(nbr_str)
# Boucle niveau 1
for i in range(1, nombre_epiceries + 1):
    total = 0.0
    # boucle niveau 2
    for j in range(1, 4):
        # Plus compliqué que d'utiliser une fstrang comme ci-haut
        montant = float(input("Entrer le montant pour épicerie " + str(i) + " pour le mois " + str(j)))
        total += montant
    print(f"Total pour épicerie {i}: {total}")



