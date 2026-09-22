def table_de_multiplication(base, initial, final):
    n = initial
    while n <= final:
        print(f"{n} * {base} = {n * base}")
        n += 1


# On peut utiliser des arguments nommés pour les passer dans le désordre
# À éviter sauf lors de l'utilisation de paramètres optionels.
table_de_multiplication(initial=1, final=5, base=8)
table_de_multiplication(base=8, initial=1, final=5)
