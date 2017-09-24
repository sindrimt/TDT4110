import math
print("Velkommen til derivasjonskalkulatoren!")
print()
x=float(input("Skriv inn verdien til x som desimaltall: "))
h=float(input("Skriv inn verdien til h som desimaltall: "))



f1 = float(math.sin(x))
f2 = float(math.sin(x + h))

derivate = (f2 - f1) / h

print("Den deriverte er: ",format(derivate,".3f"))