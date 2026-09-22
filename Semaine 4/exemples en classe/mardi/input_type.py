# input(msg) retourne une str entrée par l'usager
s = input("Entrer une phrase: ")
print(type(s))

# pour convertir une str en int, on utilise int(str)
# input() retourne la str de l'entier entré par l'usager et on appelle int() de cette str pour la convertir en entier
entier = int(input("Entrer un entier: "))
print(type(entier))
# Équivalent
entier_str = input("Entrer un entier: ")
entier = int(entier_str)
print(type(entier))

