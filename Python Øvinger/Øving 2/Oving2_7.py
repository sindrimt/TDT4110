funk = "x"

#Input opperasjon
def opperasjon():
    print("Velkommen til førskolekalkulatoren!")
    print("(Avslutt ved å skrive inn x) \n")
    print("Hva ønsker du å gjøre?")
    funk = input("+, -, * , /. \n")
    if (funk.lower()=="x"):
        return 0

    if (funk.lower() == "+"):
        addere()

    elif(funk.lower() == "-"):
        subtrahere()

    elif(funk.lower() == "*"):
        gange()

    elif(funk.lower() == "/"):
        dele()

    else:
        input("Feil input! \n \n")
        opperasjon()

#Input tall 1 og 2
def tall1 ():
    while True:
        try:
            x = float(input("Skriv inn ett tall \n"))
            y = float(input("Skriv inn enda ett tall \n"))
            return (x,y)
        except:
            print("Feil input! \n \n")

#Selve opperasjonen

def addere():
    x,y = tall1()
    print("Din sum er:", format((x+y), ".2f"))

    print("\n")
    opperasjon()

def subtrahere():
    x,y = tall1()
    print("Din sum er:",format((x-y), ".2f"))

    print("\n")
    opperasjon()

def gange ():
    x,y = tall1()
    print("Din sum er:",format((x*y), ".2f"))

    print("\n")
    opperasjon()

def dele():
    x,y = tall1()
    print("Din sum er:",format((x/y), ".2f"))

    print("\n")
    opperasjon()

while funk=="x":
    funk = opperasjon()