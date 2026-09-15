nombre = int(input("Nombre: "))

if nombre > 10:
    if nombre % 2 == 0:
        print(">10 pair")
    else:
        print(">10 impair")
else:
    if nombre % 2 == 0:
        print("<= 10 pair")
    else:
        print("<= 10 impair")
print("Fin")
