# Ajouter des print() pour debugger est une mauvaise idée, ça pollue la console
# Utilsier le debugger à la place
for i in range(15):
    print("i", i)
    for j in range(1, 5):
        print("j", j)
        if i % j == 0:
            print(f"{i} est divisible par {j}")

