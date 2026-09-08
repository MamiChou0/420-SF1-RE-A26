# le elif (else if) est une condition de plus évaluée si le if est faux...

nombre = int(input("Nombre: "))

if nombre > 10:
    print("Plus grand que 10")
elif nombre < 10:
    print("Plus petit que 10")
else:
    print("Est égal à 10")

