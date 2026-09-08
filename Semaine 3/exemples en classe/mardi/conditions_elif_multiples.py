# On peut mettre plus qu'un elif... if est évalué, si faux ensuite le premier elif, si faux le deuxième elif, etc
nombre = int(input("Nombre: "))

if nombre > 10:
    print("plus grand que 10")
elif nombre % 2 == 0:
    print("Pair <= 10")
elif nombre < 0:
    print("Négatif non pair")
else:
    print("Impair positif < 10")
