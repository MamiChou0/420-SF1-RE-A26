import matplotlib.pyplot as plt
import math


def n_log_n(n):
    return n * math.log(n)


def lineaire(n):
    return 2 + n


def exponentielle(n):
    return 2**n


def polynomiale(n):
    return n**3


coords_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y_log = []
for x in coords_x:
    y_log.append(n_log_n(x))

y_lin = []
for x in coords_x:
    y_lin.append(lineaire(x))

y_expo = []
for x in coords_x:
    y_expo.append(exponentielle(x))

y_poly = [polynomiale(x) for x in coords_x]


# https://matplotlib.org/stable/gallery/color/named_colors.html
# https://matplotlib.org/stable/api/markers_api.html
plt.plot(coords_x, y_log, color="limegreen", marker="P")
plt.plot(coords_x, y_lin, color="teal", linestyle="--", marker="h")
plt.plot(coords_x, y_expo, color="khaki", marker="d")
plt.plot(coords_x, y_poly, color="coral", marker="<")

plt.title("Fonctions mathématiques")
plt.legend(["y = x log x", "y = 2 + x", "y = 2 ** x", "y = x ** 3"])
plt.xlabel("x")
plt.ylabel("y")
plt.show()
