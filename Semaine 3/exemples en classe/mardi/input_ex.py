# input(str) permet d'afficher la str à la console pour demander une entrée de l'utilisateur, ceci retourne une str
age = input("Quel est votre âge? ")
print(age)

# On peut convertir en une ligne l'input (une str) en numérique
quantite1 = float(input("Entrer la première quantité: "))
quantite2 = float(input("Entrer la deuxième quantité: "))
print("Somme des quantités:", quantite1+quantite2)

# Si on ne convertit pas, les deux str seront concatenés
n1 = input("Nombre1: ")
n2 = input("Nombre2: ")
somme = n1 + n2
print(f"Somme (bogue): {somme}")





