# input retourne une str que l'on convertit en float
note = float(input("Entrez votre note: "))

if note >= 90:
    print("Votre avez obtenu un A")
elif 80 <= note < 90:
    print("Votre avez obtenu un B")
elif 70 <= note < 80:
    print("Votre avez obtenu un C")
elif 60 <= note < 70:
    print("Votre avez obtenu un D")
else:
    print("Votre avez obtenu un F, vous devriez vraiment étudier plus!")

