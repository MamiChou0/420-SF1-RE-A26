import matplotlib.pyplot as plt

xs = ["A", "B", "C", "D"]
ys = [42, 64, 12, 89]

plt.bar(xs, ys, color="yellow")
plt.title("Graphique à barres")
plt.xlabel("Catégories")
plt.ylabel("Valeurs")
plt.show()

plt.barh(xs, ys, color="pink")
plt.title("Barres horizontales")
plt.ylabel("Catégories")
plt.xlabel("Valeurs")
plt.show()

