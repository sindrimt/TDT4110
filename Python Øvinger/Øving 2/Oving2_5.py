def start():
    print("Hvor mye poeng fikk du på forrige eksamen?")
    poeng = float(input("Poeng skal oppgis i heltall fra 0-100: "))
    checkNr(poeng)

def checkNr(poeng):
    if (poeng%1!=0 or poeng > 100 or poeng < 0):
        poeng =float(input(("Feil input. Prøv igjen.")))
        checkNr(poeng)
    else:
        poengG(poeng)

#Poenggrense
def poengG(poeng):

    if 100 >= int(poeng) >= 89 :
        print("Gratulerer du fikk en A")

    elif 88 >= int(poeng) >= 77 :
        print("Du fikk en B")

    elif 76 >= int(poeng) >= 65 :
        print("Du fikk en C")

    elif 64 >= int(poeng) >= 53 :
        print("Du fikk en D")

    elif 52 >= int(poeng) >= 41 :
        print("Du fikk en E")

    elif 40 >= int(poeng) >= 0 :
        print("Du fikk en F")

start()
