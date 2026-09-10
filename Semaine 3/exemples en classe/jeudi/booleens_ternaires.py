nombre = int(input("Entrez un nombre: "))

print(0 <= nombre < 10)
# Équivalent, PyCharm va suggérer de la simplifier à la forme précédente
print(0 <= nombre and nombre < 10)

