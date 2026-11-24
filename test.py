import random
from random import randint


liste_loot = ['or', 'potion', 'amulette', 'épée']


def creer_gobelin() -> dict:
    gobelin = {
        'hp': randint(2, 8),
        'att': randint(1, 2),
        'def': randint(0, 1)
    }
    return gobelin

def creer_heros() -> dict:
    heros = {
        'hp': randint(15, 30),
        'att': randint(5, 7),
        'def': randint(1, 5),
        'inventaire': []
    }
    return heros

def creer_dragon() -> dict:
    dragon = {
        'hp': randint(25, 35),
        'att': randint(3, 6),
        'def': randint(3, 4)
    }
    return dragon

def combat(heros: dict, monstre: dict):
    hp_heros = heros['hp']
    hp_monstre = monstre['hp']

    print('Combat entre le héro et un', monstre['nom'])
    while hp_heros > 0 and hp_monstre > 0:
        attaque_heros = heros['att'] * randint(1, 2)
        defense_monstre = monstre['def']
        hp_monstre -= attaque_heros - defense_monstre
        print('Le héros attaque le monstre pour', attaque_heros)
        print(f'Il reste {hp_monstre} au', monstre['nom'])

        attaque_monstre = monstre['att'] * random.uniform(1.0, 2.0)
        def_heros = heros['def']
        hp_heros -= attaque_monstre - def_heros

    if hp_heros < 0:
        print('Bro is dead')
        exit()

    print('Le héros a gagné')
    heros['hp'] = hp_heros
    item_loot = random.choice(liste_loot)
    if item_loot == 'potion':
        guerison = randint(10, 15)
    elif item_loot == 'or':

