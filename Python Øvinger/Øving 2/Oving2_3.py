a = int(input("Skriv inn et tall"))
b = int(input("Skriv inn enda et tall"))

add = a+b
mult = a*b

if add>mult:
    print(a,"+",b,"er større enn",a,"*",b)

elif add<mult:
    print(a,"+",b,"er mindre enn",a,"*",b)

else:
    print(a,"+",b,"er likt",a,"*",b)

svar = int(input("Hva er 3 ganget med 4?"))

if svar==12:
    print("Riktig!")

else:
    print("Feil!")



