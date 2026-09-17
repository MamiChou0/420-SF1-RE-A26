import matplotlib.pyplot as plt

# On se fait une liste de coordonnées
coords_x = [1, 2, 3, 4, 5]
coords_y = [42, 5, 3, 7, 24]

x1 = [1, 2, 6, 10, 20]
y1 = [150, 23, 54, 2, 8]

plt.plot(coords_x, coords_y, color="blue", linestyle="--", marker="*")
plt.plot(x1, y1, color="springgreen", linestyle="-.", marker="P")

plt.title("y en fonction x")
plt.legend(["Courbe 1", "courbe verte"])

plt.xlabel("Axe des x")
plt.ylabel("Axe des y")
plt.xlim(1, 25)
plt.ylim(0, 165)

plt.show()

plt.plot(x1, y1, "r--o")
plt.show()

