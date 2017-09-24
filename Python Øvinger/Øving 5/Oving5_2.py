#Spørreundersøkelse

antall_kvinner = 0
antall_menn = 0
antall_fag = 0
antall_ITGK = 0
antall_timer_lekser = 0



def start ():
    alder = age()
    kjonn = k_m()
    fag = skole()
    if fag =="ja":
        variabelmedlem_ITGK = itgk(alder)
        timer_lekser = timer()
    print("Takk for at du tok deg tid til å svare på spørreundersøkelsen. \n \n \n \n")

    start()

def age ():
    alder = int(input("Hvor gammel er du? Angis i heltall. "))
    if alder ==1414:
        stats()
    elif alder < 16 or alder > 25:
        print("Beklager, du er ikke i målgruppen for denne spørreundersøkelsen. \n ")
        start()
    elif alder >= 16 and alder <= 25:
        return alder

    else:
        print ("Du skrev feil input. Prøv igjen. \n ")
        age()

def k_m ():
    kjonn = input("Trykk 'k' for kvinne og 'm' for mann: ")
    if kjonn == "k":
        global antall_kvinner
        antall_kvinner += 1
        return kjonn
    elif kjonn == "m":
        global antall_menn
        antall_menn += 1
        return kjonn

    else:
        print ("Du skrev feil input. Prøv igjen. \n ")
        k_m()

def skole ():
    fag = input("Tar du noen fag? 'Velg ja/nei'")
    if fag=="ja":
        global antall_fag
        antall_fag += 1
        return fag
    elif fag =="nei":
        return fag
    else:
        print ("Du skrev feil input. Prøv igjen. \n ")
        skole()

def itgk (alder):
    if alder <22:
        it = input("Tar du ITGK? - 'Velg ja/nei' ")
        if it == "ja":
            global antall_ITGK
            antall_ITGK += 1
            return it
        elif it == "nei":
            return it

    elif alder >=22:
        it = input("Tar virkelig du ITGK? - 'Velg ja/nei' ")
        if it == "ja":
            antall_ITGK += 1
            return it
        elif it == "nei":
            return it
    else:
        print ("Du skrev feil input. Prøv igjen. \n ")
        itgk()


def timer ():
    tid = eval(input("Hvor mange timer bruker du i snitt på lekser? Avgis i heltall."))
    if tid >=0 and tid < 25:
        global antall_timer_lekser
        antall_timer_lekser += tid
        return tid
    else:
        print ("Du skrev feil input. Prøv igjen. \n ")
        timer()


def stats():
    global antall_kvinner,antall_menn,antall_fag,antall_ITGK,antall_timer_lekserl

    print("Antall kvinner:",antall_kvinner)
    print("antall menn:",antall_menn)
    print("antall som tar fag:",antall_fag)
    print("antall som tar ITGK:",antall_ITGK)
    print("antall timer lekser totalt:", antall_timer_lekser)
    print("\n \n \n \n")

start()