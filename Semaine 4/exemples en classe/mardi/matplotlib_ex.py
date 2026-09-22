import matplotlib.pyplot as plt

coords_x = [4, 5, 6, 7, 8]
coords_y = [42, 64, 2, 145, 3]
coords_3 = [49, 84, 24, 148, 4]

coords_x_2 = [43, 77, 1, 6, 9, 126]
coords_y_2 = [23, 54, 12, 156, 48, 99]

plt.plot(coords_x, coords_y, color="red", linestyle="-", marker="*")
plt.plot(coords_x_2, coords_y_2, color="green", linestyle="--", marker="o")
plt.plot(coords_x, coords_3, "y--v")

plt.legend(["Courbe 1", "Courbe 2", "Courbe 3"])

plt.title("Titre du graphique")
plt.xlabel("Axe des x")
plt.ylabel("Axe des y")

plt.xlim(1, 130)
plt.ylim(1, 180)

plt.show()


