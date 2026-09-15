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

