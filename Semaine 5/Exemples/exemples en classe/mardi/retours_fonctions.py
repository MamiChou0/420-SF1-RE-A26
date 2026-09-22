import math
# Certaines fonctions ne retournent rien, ce sont techniquement des procédures
# ex:
def bonjour(nom):
    print(f"Bonjour {nom}!")
# Autre ex:
retour = print("Allo")
print(retour)


# On peut retourner une ou plusieurs valeurs
# ici on retourne un float
def pythagore(base, hauteur):
    # math.sqrt retourne la racine carrée qui est un float
    h = math.sqrt(base**2 + hauteur**2)
    return h


hypothenuse = pythagore(3, 4)
print(f"hypothénuse: {hypothenuse}")

# input() retourne une str
retour_input = input("Entrez une phrase: ")
print(retour_input)


# Ex: Calcul du sinus d'un angle de 30 degrés
# math.sin() utilise des gradians, on doit convertir notre angle donné en degrés en radians
# math.radians(degrés) convertit un angle vers les radians
angle_en_degres = 30.0
# on assigne le retour de math.radians() à angle_en_radians
angle_en_radians = math.radians(angle_en_degres)
# On assigne le retour de math.sin() à sinus
sinus = math.sin(angle_en_radians)
print(f"Sinus de {angle_en_degres} degrés = {sinus}")

