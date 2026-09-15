import time

max = 1000000

iterations = 0
compteur = 0
debut = time.perf_counter_ns()

for i in range(0, max):
    iterations += 1
    print(f"itérations: {iterations}")
    if i % 2 == 0:
        compteur += 1
print(f"Compteur {compteur}, itérations {iterations}")
temps_fin_1 = time.perf_counter_ns() - debut
print(f"Temps d'exécution: {temps_fin_1} ns")

iterations = 0
compteur = 0
debut = time.perf_counter_ns()

for i in range(0, max, 2):
    iterations += 1
    print(f"itérations: {iterations}")
    compteur += 1
print(f"Compteur {compteur}, itérations {iterations}")
temps_fin_2 = time.perf_counter_ns() - debut
print(f"Temps d'exécution: {temps_fin_2} ns")

print(f"V1: {temps_fin_1}\tV2: {temps_fin_2}")
