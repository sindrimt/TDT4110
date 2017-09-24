def readOneNumber():
    rad = int(input("Rad (1-9)"))
    kolonne = int(input("Kolonne (1-9)"))
    tall = int(input("Tall (1-9)"))

    print("Posisjon: (%d,%d) inneholder nå %df"%(rad,kolonne,tall))




def readPositionDigit(rowNr,colNr,board):
    board[rowNr-1][colNr-1] = int(input("Hvilket tall vil du ha på (%d,%d)?"%(rowNr,colNr)))
    print ("Verdi for posisjon (%d,%d) er nå %d"%(rowNr,colNr,board[rowNr-1][colNr-1]))



#readPositionDigit(2,3,[[1,0,0],[2,0,0],[3,0,0]])

def readValidPositionDigit(rowNr,colNr,board):
    VALID_NR = list(range(0,10))

    while(True):
        try:
            number = int(input("Hvilket tall vil du ha på (%d,%d)?"%(rowNr,colNr)))
            if number not in VALID_NR:
                print("Skriv et tall mellom 0-9.")
                continue
            break
        except Exception:
            print("Feil input! Det var ikke et tall")
            continue

    board[rowNr-1][colNr-1] = number
    print ("Verdi for posisjon (%d,%d) er nå %d"%(rowNr,colNr,board[rowNr-1][colNr-1]))

    return board

        
#readValidPositionDigit(2,3,[[1,0,0],[2,0,0],[3,0,0]])

def readSudokuBoard(board):


    for row in range(1,len(board)+1):
        for col in range(1,len(board[0])+1):
            answer = input("Nummer %d er på posisjon (%d,%d). Ønsker du å endre? (Y/N) "%(board[row-1][col-1],row,col) )
            if answer.upper() == "YES" or answer.upper()=="Y":
                board = readValidPositionDigit(row,col,board)
            elif answer.upper() =="NO" or answer.upper()=="N":
                continue


    return board

"""
print (readSudokuBoard(
[[1, 2, 3, 4, 5, 6, 7, 8, 9],
 [2, 3, 4, 5, 6, 7, 8, 9, 1],
 [3, 4, 5, 6, 7, 8, 9, 1, 2],
 [4, 5, 6, 7, 8, 9, 0, 1, 2],
 [3, 4, 5, 6, 7, 8, 9, 0, 1],
 [2, 3, 4, 5, 6, 7, 8, 9, 0],
 [1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8],
 [9, 0, 1, 2, 3, 4, 5, 6, 7]]))

"""

#oppgave 4





def bidOK (meldt,resultat):
    meldt = meldt.split()
    tall = float(meldt[0][:2])

    if tall+6 <= resultat:
        return True
    else:
        return False

#print(bidOK ("4 ruter",10))

def utgang (meldt,resultat):
    temp = meldt.split()
    meldt_poeng = int(temp[0][0:])
    trumf = str(temp[1][0:])


    if bidOK(meldt,resultat)==True:
        

        if trumf.upper() == "GRAND" and ((resultat) >=9) and meldt_poeng>= 3:
            return True

        elif (trumf.upper() == "HJERTER" or trumf.upper() == "SPAR") and ((resultat) >= 10) and (meldt_poeng>= 4):
            return True

        elif (trumf.upper() == "KLØVER" or trumf.upper() == "RUTER") and ((resultat)>= 11) and (meldt_poeng>= 5):
            return True

        else:
            return False

    else:
        return False

    
#print(utgang("3 grand",9))

def poeng_trekk(meldt,resultat):
    meldt = meldt.split()
    antatt_poeng = float(meldt[0][0:])
    poeng = resultat-6
    trumf = str(meldt[1][0:])

    if trumf.upper()=="KLØVER" or trumf.upper()=="RUTER":
        return (poeng * 20)
    elif trumf.upper()=="HJERTER" or trumf.upper()=="SPAR":
        return (poeng * 30)
    else:
        return (poeng * 30)+10

def bridgePoints(meldt,resultat):

    if utgang(meldt,resultat) == True:
        return (300+poeng_trekk(meldt,resultat))

    elif utgang(meldt,resultat) == False:
        if bidOK(meldt,resultat) == True:
            return (50+poeng_trekk(meldt,resultat))
        else:
            return -50

#print(bridgePoints('3 ruter', 10))


"""
bridgePoints( '3 ruter', 10) 130
bridgePoints( '3 ruter', 8) -50
bridgePoints( '3 spar', 12) 230
bridgePoints( '4 spar', 12)480
bridgePoints( '4 grand', 12)
490
"""
        
        
    
def main ():
    lagnavn = ["N/S","Ø/V"]
    spill = []
    tot = []
    for lag in range (1,3):
        temp = []
        print("Lag %s"%(lagnavn[lag-1]))
        meldt = input("Melding? (eks. 3 ruter)")
        resultat = int(input("Hva ble resultatet? (eks. 10)"))
        temp.extend((lagnavn[lag-1],meldt,resultat,bridgePoints(meldt,resultat)))
        spill.append(temp)
        tot.append(temp[3])
    print(("Totalt ble det utdelt %d-poeng. %d-poeng til %s og %d-poeng til %s")%(sum(tot),tot[0],lagnavn[0],tot[1],lagnavn[1]))
    return spill

print(main())











    
