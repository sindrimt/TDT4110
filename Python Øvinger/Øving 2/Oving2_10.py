def wholeNumber():
    print("\n")
    nr = float(input("Skriv inn tall: \n"))
    if (nr % 1==0):
        print("Dette er et heltall")
        evenNumber(nr)
    elif(nr % 1!=0):
        print("Dette er ikke et heltall")
        evenNumber(nr)
    else:
        wholeNumber()

def evenNumber(nr):
    if(nr % 2==0):
        print("Dette er et partall")
        sign(nr)

    elif(nr % 2==1):
        print("Dette er et oddetall")
        sign(nr)

    else:
        sign(nr)

def sign(nr):
    if(nr >= 0):
        print("Tallet er positivt")
        wholeNumber()
    elif(nr <0):
        print("Tallet er negativt")
        wholeNumber()
    else:
        wholeNumber()

wholeNumber()