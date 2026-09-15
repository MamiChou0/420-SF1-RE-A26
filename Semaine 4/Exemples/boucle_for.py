
# range(10) génère une séquence de 0 à 9; range(fin non incluse)
# for i in range(10):
#     print(i)


nombre = int(input("Entrez un nombre: "))
print("Table de multiplication de ", nombre)

print("*" * 20)
# range(debut inclus, fin non incluse) génère une séquence de début jusqu'à la fin non incluse
for base in range(1, 11):
    print(f"{base} * {nombre} = {base*nombre}")

print("*" * 20)
