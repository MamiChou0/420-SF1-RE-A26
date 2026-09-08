# Mettre deux conditions if de suites n'est pas la même chose qu'un if elif else

nombre = int(input("Nombre: "))

if nombre > 10:
    print("plus grand que 10")
if nombre % 2 == 0:
    print("Pair")
else:
    print("Impair")

if nombre > 10:
    print("nb plus grand que 10")
elif nombre % 2 == 0:
    print("nb pair <= 10")
else:
    print("autre")
