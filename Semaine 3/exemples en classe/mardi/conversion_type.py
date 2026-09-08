# En python, il y a une différence entre 123 et "123"

# Pour convertir un entier (int) en str, on utilise la fonction str
valeur = 42
valeur_en_str = str(valeur)

# Pour convertir une str en int, on utilise int()
str_numerique = "12345"
entier = int(str_numerique)

# Pour convertir en float, on utilise float()
str_float = "3547.96"
mon_float = float(str_float)

# Ceci donnera une erreur, décommentez pour tester
str_int_non_valide = "456H65"
# entier_erreur = int(str_int_non_valide)

# On peut aussi convertir entre les int et les float
mon_int = 39847543
float_du_int = float(mon_int)

mon_float2 = 546.78
mon_int_du_float = int(mon_float2)

pass



