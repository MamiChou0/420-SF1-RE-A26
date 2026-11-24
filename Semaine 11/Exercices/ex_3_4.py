heros = {
    'nom': 'Aria',
    'classe': 'magicienne',
    'niveau': 1,
    'stats': {'force': 4, 'magie': 9, 'agilité': 6}
}


def afficher_personnage(perso: dict):
    print(f'{perso['nom']}, {perso['classe']}')