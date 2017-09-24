def les_inn_bilinfo():
    vitne = []
    vitne.append(input("Hvilken bil var det?"))
    vitne.append(input("Hvilken modell?"))
    vitne.append(input("Hvilken farge?"))

    return vitne

def sjekk_bil(vitne,orginal):

    for i in range(3):
        if vitne[i]=="?":
            continue
        if (vitne[i]!=orginal[i]):
            return False
    return True



sjekk_bil(["FIAT","Uno","Rø"],["FIAT","Uno","Rød"])


def les_gyldig_vitneskilt():
    SKILTBOKSTAV = ('A','B','C','D','E','F','G','H','J','K','L','N','P','R','S','T','U','V','X','Y','Z','?')
    TALL = ('1','2','3','4','5','6','7','8','9','0','?')


    skilt = input("Skriv inn skilt. 2-boks. 5-tall ('?' for usikker)")

    if len(skilt)!=7:
        print("Det må være minst 7 tegn.")
        skilt = les_gyldig_vitneskilt()

    for bokstav in skilt[0:2]:
        if not(bokstav.upper() in SKILTBOKSTAV):
            print('To første tegn må være bokstaver eller "?" ')
            skilt = les_gyldig_vitneskilt()


    for tall in skilt[2:]:
        if not(tall in TALL):
            print('De fem siste tegnene må være tall eller "?" ')
            skilt = les_gyldig_vitneskilt()

    return skilt.upper()



def match (vitne_observasjon,skilt):
    for i in range(0,7):
        if (vitne_observasjon[i]!=skilt[i] and vitne_observasjon[i]!='?'):
            return False
    return True


def match_liste (vitne_observasjon,skilt):
    suspects =[]
    #for i in range(len(skilt)):
    for nummer in skilt:
        sjekk = match(vitne_observasjon,nummer)
        if sjekk==True:
            suspects.append(nummer)

    return suspects

#match_liste('VF???55',['VX33322','VF12355','VF77455','DA?????','VF10055'])


def main (filnavn):
    try:
        with open(filnavn,'r') as bilinfo:
            db = {}
            liste = bilinfo.readlines()
            liste1 = []
            for i in range (len(liste)):
                liste1.append(liste[i].strip())
            for n in liste1:
                templist= n.split(" ")
                db[templist[0]]=templist[1:]


    except FileNotFoundError:
        print("Filen",filnavn, "finnes ikke")
    else:
        vitne_obs = []
        vitne_reg = ""

        while (True):
            vitne_obs.append(les_inn_bilinfo())
            vitne_reg =(les_gyldig_vitneskilt())
            x = input("Vil du sjekke flere kjøretøyer? (Y/N)")
            if x.upper()=="N":
                break
        print(db.keys())
        print(vitne_reg)
        suspects = match_liste(vitne_reg,db.keys())
        print(suspects)

        #UFERDIG HER!


main('biler.txt')
