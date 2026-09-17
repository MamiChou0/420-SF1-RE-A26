# L'utilisation d'un debugger est toujours à privilégier sur les print()

nbr_str = input("Nombre épiceries: ")
nombre_epiceries = int(nbr_str)
# Boucle niveau 1
for i in range(1, nombre_epiceries + 1):
    print("i", i)
    total = 0.0
    # boucle niveau 2
    for j in range(1, 4):
        print("j", j)
        montant = float(input(f"Entrer le montant pour épicerie {i} pour le mois {j}"))
        total += montant
    print(f"Total pour épicerie {i}: {total}")