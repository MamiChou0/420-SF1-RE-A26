phrase = input('Phrase : ').replace(' ', '').lower()

frequences = {}

for lettre in phrase:
    frequences[lettre] = frequences.get(lettre, 0) + 1
print(frequences)

plus_frequente = max(frequences, key=frequences.get)
print(f'Lettre la plus fréquente : {plus_frequente} ({frequences[plus_frequente]} fois)')
