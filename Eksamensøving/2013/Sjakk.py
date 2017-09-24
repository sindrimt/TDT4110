def chess_match():
    total_score1 = 0
    total_score2 = 0
        
    num_games = int(input("Hvor mange partier skal spilles?"))
    if num_games < 1:
        print("Så kjedelig, da blir det ingen kamp!")
    else:
        game = 1
    while game <= num_games:
        print("Parti %d"%(game))

        score1= int(input("Antall poeng til spiller 1 i partiet?"))
        score2= int(input("Antall poeng til spiller 2 i partiet?"))
        game += 1
        total_score1 += score1
        total_score2 += score2

    print ("Kampen er slutt!\nSpiller 1 fikk totalt %d-poeng.\nSpiller 2 fikk totalt %d-poeng. " %(total_score1,total_score2))
    
def end_of_match(num_games, game, total_score1, total_score2):
    if total_score1 > (num_games/2):
        return 1
    elif total_score2 > (num_games/2):
        return 2
        
    if num_games==game:
        if total_score1 == total_score2:
            return 3
        elif total_score1 > total_score2:
            return 1
            
        elif total_score1 < total_score2:
            return 2            
    else:
        return 0

def chess_scorer():
    MULIGE_POENG = (1,0.5,0)
    while True:
        score1 = float(input("Hvor mange poeng fikk Spiller 1 i partiet?"))
        if score1 in MULIGE_POENG:
            break
        else:
            print("Umulig resultat!")

    if score1 == 1:
        score2 =0
    elif score1 == 0.5:
        score2 = 0.5
    else:
        score2 = 1
        
    return score1, score2

def player_score(results):
    total_score = 0.0
    for score in results:
        if score != None:
            total_score += score
    return total_score


        


#print(player_score([1,0.5,0.5,None]) ) #antar dette er hvordan results ser ut ved 4 parti



#Oppgave 4 UKA

def payment(pris,antall):

    if antall > 3:
        return pris*antall*0.9
    else:
        return pris*antall


def get_price(konsert):
    kons_info = []
    with open("prices.txt","r") as fil:
        for linje in fil:
            kons_info.append(linje.strip().split(";"))

    for info in kons_info:
        if konsert == info[0]:
            pris = float(info[1])
            return pris
    else:
        return -1

#print(get_price("The aller beste"))



def ticket(navn,konsert,antall):

    konsertpris = get_price(konsert)
    pris = payment(konsertpris,antall)


    print("UKA - BILLETT".center(34))
    print ("*"*35)
    print("Navn".ljust(20),navn)
    print("Konsert".ljust(20),konsert)
    print("Antall billetter".ljust(20), str(antall))
    print("Totalpris:".ljust(20),str(pris)+"kr")
    
    

print(ticket("Nils Nilsen","The Rectorats",8))



def write_to_file(navn,konsert,antall,filename):
    konsertpris = get_price(konsert)
    totalpris = payment(konsertpris,antall)
    with open(filname,"a") as fil:
        linje = (konsert+";"+str(antall)+";"+str(totalpris)+";"+navn)
        fil.write(linje+"\n")
        






#print(write_to_file("Nils Nilsen","The Rectorats",8,"concerts.txt"))

