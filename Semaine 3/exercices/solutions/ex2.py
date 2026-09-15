phrase = input("Entrez une phrase: ")
lettre_a_compter = input("Entrez une lettre à compter: ")

if len(lettre_a_compter) != 1:
    print("Veuillez entrer UNE lettre seulement. Fin du programme.")
else:
    print(f"La phrase:\n{phrase}\ncontient {phrase.count(lettre_a_compter)} la lettre '{lettre_a_compter}'")
