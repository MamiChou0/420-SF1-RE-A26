import time


# While True est toujours vrai
while True:
    # strftime: string format time... donne l'heure courant sous le format fourni
    print("Heure courante: ", time.strftime("%H:%M:%S"))
    reponse = input("Voulez-vous quitter [o/n]")
    # break sort de la boucle en cours
    if reponse == "o":
        break

print("fin du programme")


