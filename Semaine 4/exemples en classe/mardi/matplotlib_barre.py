import matplotlib.pyplot as plt

coords_x = [1, 2, 3, 4, 5, 6, 7]
coords_y = [32, 64, 12, 67, 89, 55, 99]

plt.bar(coords_x, coords_y)
plt.title("Nombre par catégories")
plt.xlabel("Catégories")
plt.ylabel("Nombre")
plt.show()

plt.barh(coords_x, coords_y, color="c")
plt.ylabel("Catégories")
plt.xlabel("Nombre")
plt.show()


