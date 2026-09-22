import time

total = 0
debut = time.perf_counter_ns()
for i in range(1000000):
    print(i)
    # total += i
fin = time.perf_counter_ns()
temps_total = fin - debut
print(f"Exécution de la boucle: {temps_total} ns")



