nombre = int(input("Nombre: "))

# Il peut y avoir un nombre illimité de elif entre le if et le else
if nombre < 10:
    print("plus petit que 10")
elif nombre % 2 == 0:
    print("Pair >= 10")
elif nombre % 3 == 0:
    print("impair >= 10 divisible par 3")
else:
    print("impair >= 10 non divisible par trois")

# Le code ci-haut n'est pas équivalent au code suivant:
if nombre < 10:
    print("if < 10")
if nombre % 2 == 0:
    print("if % 2")
if nombre % 3 == 0:
    print("if % 3")
else:
    print("else")  # le else ici est associé au dernier if
print("Fin")
