# On peut imbriquer des conditions, car un bloc d'instructions peut aussi contenir des conditions
nombre = int(input("Nombre? "))

if nombre < 10:
    if nombre % 2 == 0:
        print("< 10 et pair")
    else:
        print("< 10 et impair")
elif nombre > 10:
    if nombre % 2 == 0:
        print("> 10 et pair")
    else:
        print("> 10 et impair")
else:
    print("10")
print("Fin")

