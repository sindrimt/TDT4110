# Modul bruker

def velkommen():
    print('Velkommen til hybelregnskapsprogram v 3.0')
    print('=========================================')


def valgmeny():
    print('\nVelg kommando [utgift|inntekt|load|save|fjern|vis|avslutt]')
    valg = input("Kommando: ")
    return valg

def registrer(db,dbid,valg):
    print('Registrering av',valg)
    dato = input('Dato [yyyy-mm-dd]: ')
    belop = float(input('Beløp [kr]: '))
    beskrivelse = input('Beskrivelse [tekst]: ')
    if (valg=='utgift'):
        belop = belop*-1
    db[dbid] = [dato,belop,beskrivelse] #Legg inn i dictionary
    melding('Data er registrert')
    return db #Returnerer databasen (dictonary)

def melding (tekst):
    print('>>>',tekst)

def vis (db): #Vise hele regnskapet (alt i dictionary'en)
    balanse = 0
    print('ID   Dato      Beskrivelse                      Sum')
    print('==============================================================================')
    for x in db:
        liste = db[x] #Henter ut liste [dato,beløp,beskrivelse]
        s = str(x).rjust(4)+liste[0].rjust(11) #ID og dato
        s += ' '+liste[2].ljust(30) #Beskrivelse venstrejuster 30 tegn
        s += str(liste[1]).rjust(8) #Beløp, høyrejustert 8 tegn
        print(s) #Skriver ut tekst streng med alle
        balanse = balanse + liste[1]
    print('Balanse:',balanse)

def fjern (db):
    print('IDer i databasen: ',db.keys())
    dbid = int(input("ID på innslag som skal fjernes: "))
    if (dbid in db): #Sjekke om dbid finnes i db
        del db[dbid] #Fjerne innslag fra dictionary
        melding('Innslag med ID'+str(dbid)+'er fjernet')
    else:
        melding('ID'+str(dbid)+'finnes ikke i databasen')
    return db

def velgfilnavn():
    filnavn = input('Velg filnavn: ')
    return filnavn

