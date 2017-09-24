import random

def throw (n):
    dice = []

    for x in range(0,n):
        dice.append(random.randint(1,6))

    return dice

throw(5)


def chance(dice):
    sum_dice = 0

    for x in dice:
        sum_dice += x



    return sum_dice

chance([5, 2, 6, 3, 3])


def house(dice):
    dice_unik = set(dice)
    dice_unik = list(dice_unik)
    dice.sort()

    if len(dice_unik) ==2:
        if dice[0]==dice[1] or dice[3]==dice[4]:
            return sum(dice)
        else:
            return 0
    else:
        return 0

house([1,3,1,1,3])

def straight (dice):
    dice.sort()

    if dice == [1,2,3,4,5]:
        return 15
    elif dice == [2,3,4,5,6]:
        return 20
    else:
        return 0

straight([5,6,4,2,3])

#OPPGAVE 4


def les_inn_bilinfo():
    vitne_info = []
    vitne_info.append(input("Hvilket bilmerke var det?"))
    vitne_info.append(input("Hvilken modell?"))
    vitne_info.append(input("Hvilken farge?"))

    return vitne_info

#les_inn_bilinfo()

def sjekk_bil(vitne,orginal):
    for x in vitne:
        if x not in orginal and x != "?":
            return False

    return True



sjekk_bil(['FIAT','Uno','?'],['FIAT','Uno','Rød'])


def les_gyldig_vitneskilt():
    SKILTBOKSTAV = ('A','B','C','D','E','F','G','H','J','K','L','N','P','R','S','T','U','V','X','Y','Z','?')
    SKILTTALL = ['1','2','3','4','5','6','7','8','9','0','?']

    vitne_skilt = input("Skriv inn skilt, 2 bokst + 5 tall (?=usikker)")

    if len(vitne_skilt) != 7:
        print("Skiltnummer må være 7 tegn langt")
        vitne_skilt = les_gyldig_vitneskilt()

    for bokstav in vitne_skilt[0:2]:
        if (bokstav.upper() not in SKILTBOKSTAV):
            print("To første tegn må være lovlig skiltbokstav eller ?")
            vitne_skilt = les_gyldig_vitneskilt()
        
    for tall in vitne_skilt[2:]:
        if (tall not in SKILTTALL) and (tall != "?"):
            print ("Fem siste tegn må være tall eller ?")
            vitne_skilt = les_gyldig_vitneskilt()
                
    return vitne_skilt.upper()


#les_gyldig_vitneskilt()

def match(vitne,orginal):
    for i in range(0,7):
        if (vitne[i] != orginal[i]) and (vitne[i] != "?"):
            return False
    else:
        return True


match('VF???55','VF12355')


def match_liste(vitne,org_liste):
    matched = []
    for x in org_liste:
        check = match(vitne,x)
        if check == True:
            matched.append(x)

    return matched

match_liste('VF???55',['VX33322','VF12355','VF77455','DA?????','VF10055'])



def main (filnavn):

    try:
        with open(filnavn,"r") as f:
            db = {}

            for linje in f:
                liste = linje.strip().split(" ")
                db[liste[0]] = liste[1:]
            print(db)
                
            print("Fil lest")

    except FileNotFoundError:
        print("fil finnes ikke")


    while(True):
        #Spør bruker om info
        vitne_info = les_inn_bilinfo()

        #Spør om skiltinfo
        vitne_skilt = les_gyldig_vitneskilt()

        #Sjekker skilt opp mot database
        match = match_liste(vitne_skilt,['VX33322','VF12355','VF77455','DA?????','VF10055'])

        cont = input("Vil du sjekke flere kjøretøyer? (J/N)")

        if cont.upper() == "N" or cont.upper() =="NEI":
            break

    if len(match) == 0 :
        print ("Ingen match")
    else:
        print("Mulige kjøretøyer på %s er %s" %(vitne_skilt,match))


print(main("biler.txt"))











































    



