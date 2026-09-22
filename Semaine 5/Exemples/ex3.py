# print() permet l'affichage
print("Vive python!")

# input() permet l'entrée d'un str par un utilisateur
ma_str = input("Entrez une phrase: ")

# abs() retourne la valeur absolue d'un numérique
print(abs(-5))

# float(), int(), str(), hex(), bytes(), bool(), oct() convertit un valeur dans un type
x = int(5.0)
y = float("5.6")
print(x, y)

conditions = [True, 5 > 4, 1, True]
# all() retourne True si tous les éléments de la séquence sont vrais
print(all(conditions))

conditions_2 = [True, 6 > 7, 0, False]
# any() retourne True si une des éléments de la séquence est vrai
print(any(conditions_2))
