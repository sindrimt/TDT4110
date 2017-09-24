#Hovedmodulen
#Importerer moduler som skal brukes i main

import bruker #Brukergrensesnitt
import fil  #Filbehandling

#Opprette variabler og initialer (gi dem verdier)

db = {} #Oppretter et tomt dictionary
dbid = 0 # Id til dictionary som settes til 0

# Gi en vellkomst til bruker
bruker.velkommen() #Velkomstmelding til bruker

#Gi en valgmeny til bruker
valg = bruker.valgmeny() #Lar bruker velge hva h*n skal gjøre

while(valg !='avslutt'): #Løkke helt til 'avslutt' er valgt.
    if (valg=='utgift' or valg=='inntekt'):
        dbid += 1 #Øker databaseid med 1
        db = bruker.registrer(db,dbid,valg)

    elif (valg=='vis'): #Viser databasen
        bruker.vis(db)

    elif(valg=='fjern'): #Fjern innslag i dictionary
        db = bruker.fjern(db)

    elif(valg=='save'): #Lagre dictionary til fil
        filnavn = bruker.velgfilnavn()
        fil.save(db,filnavn)
        bruker.melding('Database er lagret i '+filnavn)

    elif(valg=='load'): #Laster dictionary fra fil
        filnavn = bruker.velgfilnavn()
        db = fil.load(filnavn) #Henter dictionary fra fil
        dbid = max(db) #Finner største id
        bruker.melding(filnavn+' er lastet inn.')

    else:
        bruker.melding("Feil kommando")
    valg = bruker.valgmeny()