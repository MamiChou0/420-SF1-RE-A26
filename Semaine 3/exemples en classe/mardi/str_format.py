# La fonction format permet de formatter et effectuer des substitutions de {}
ma_str = "L’essentiel est invisible pour les {}, on ne voit bien qu'avec le {}."
print(ma_str.format("yeux", "coeur"))
print(ma_str.format("genoux", "pied"))

# Cependant, il est préférable d'utiliser les format strings ou fstrings, on utilise le préfixe f avant la str
espace_str = "espace"
coeur_str = "coeur"
citation = f"L’amour, c’est l’{espace_str} et le temps rendus sensibles au {coeur_str}."
print(citation)

# Les fstring peuvent être utilisées pour formatter, entre autres, des nombres
mon_nombre = 42.768594030
# g permet de garder un nombre globale de "nombres" (entier + décimales)
print(f"Mon nombre est: {mon_nombre:.5g}")
# f permet de garder un nombre de décimales
print(f"Mon nombre est: {mon_nombre:.5f}")





