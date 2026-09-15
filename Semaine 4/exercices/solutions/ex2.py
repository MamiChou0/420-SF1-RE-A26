liste_nombre = [42, 54, 47, 89, 666, 31, 34, 23, 99]

nb_pairs = 0
nb_impairs = 0

for i in liste_nombre:
    if i % 2 == 0:
        nb_pairs += 1
    else:
        nb_impairs += 1

print(f"Liste: {liste_nombre}\nNombre de pairs {nb_pairs}\nNombre d'impairs {nb_impairs}")
