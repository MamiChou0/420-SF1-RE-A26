def table_de_multiplication(base, initial, final):
    n = initial
    while n <= final:
        print(f"{n} * {base} = {n * base}")
        n += 1


table_de_multiplication(5, 1, 10)
print("*" * 10)
table_de_multiplication(4, 5, 20)

