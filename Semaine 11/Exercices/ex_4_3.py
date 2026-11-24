import string

phrase = input('Phrase : ')
lettres_presentes = {lettre for lettre in phrase.lower()}
lettres_alphabet = {lettre for lettre in string.ascii_lowercase}
lettres_manquantes = lettres_alphabet - lettres_presentes

if lettres_manquantes == set():
    print("C'est un pangramme !")
else:
    print('Pas un pangramme. Lettres manquantes :', ' '.join(sorted(lettres_manquantes)))
