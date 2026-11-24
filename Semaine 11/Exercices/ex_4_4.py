ingredients_requis = {'herbe', 'miel', 'cristal', 'eau'}
ingredients_possedes = set(input('Ingrédients : ').split(','))
ingredients_manquants = ingredients_requis - ingredients_possedes
ingredients_surplus = ingredients_possedes - ingredients_requis

if ingredients_manquants == set():
    print('Potion prête !')
else:
    print('Il manque :', ', '.join(ingredients_manquants))
if ingredients_surplus == set():
    print('Aucun surplus')
else:
    print('Inutiles :', ', '.join(ingredients_surplus))
