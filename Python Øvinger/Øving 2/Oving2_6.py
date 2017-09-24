#VALG AV VALUTA
def valuta():
    print("Hvilken valuta ønsker du å veksle til?")
    change = input("EUR - GBP - RUB: \n ")
    print("Dagens valuta er: \n ")
    print("NÅ:       EUR: 8,7 -"," GBP: 11,9 - ","RUB: 0,14")
    print("SENERE:   EUR: 9,1 - ", "GBP: 12,5 - ","RUB: 0.15 \n \n")

    CheckValuta(change)

#SJEKKER INPUT
def CheckValuta(change):

    if (change.lower()=="eur"):
        change = "EUR"
        print("Du valgte EUR \n")
        ExWhen(change)
    elif (change.lower()=="gbp"):
        change = "GBP"
        print("Du valgte GBP \n")
        ExWhen(change)
    elif (change.lower()=="rub"):
        change = "RUB"
        print("Du valgte RUB \n")
        ExWhen(change)

    #FEIL INPUT
    else:
        print("Dette er ikke en gyldig valuta. \n \n")
        valuta()

#HVOR OG NÅR
def ExWhen (change):
        print("Ønsker du å veksle i bank eller ved annkomst?")
        print("- Banken har 5% vekslingsgebyr og flyplassen 10%.")
        time = input("BANK - FLYPLASS \n")

        #NÅR - BANK
        if (time.lower()=="bank"):
            print("Når ønsker du å veksle?")
            #SLEKKER RIKTIG INPUT
            while time !=(1 or 2):
                time = input("NÅ - SENERE \n")
                if(time.lower()=="nå"):
                    time=1
                    Value(change,time)
                elif(time.lower()=="senere"):
                    time=2
                    Value(change,time)



        #NÅR - FLYPLASS
        elif (time.lower()=="flyplass"):
            print("Når ønsker du å veksle?")
            while time !=(3 or 4):
                time = input("NÅ - SENERE \n")
                if(time=="NÅ" or time=="nå"):
                    time=3
                    Value(change,time)
                elif(time=="SENERE" or time=="senere"):
                    time=4
                    Value(change,time)
        #FEIL INPUT
        else:
            print("Feil input! \n \n")
            ExWhen(change)

#Hvor mye skal veksles
def Value(change,time):
    print("Hvor mye ønsker du å veksle?")
    value = input("Oppgis i heltall: \n ")
    if value.isdigit():
        value = int(value)
        print("Du ønsker å veksle : ",value,"kr ","til: ",change,"\n" ,sep='')
        ExchangeNow(change,time,value)
    else:
        print("Feil input! \n \n")
        Value(change,time)

#Veksling
def ExchangeNow(change,time,value):
    #BANK NÅ
    if(time==1):
        if(change=="EUR"):
            value=(value/8.7)*0.95
            end(value,change)
        if(change=="GBP"):
            value=(value/11.9)*0.95
            end(value,change)
        if(change=="RUB"):
            value=(value/0.14)*0.95
            end(value,change)

    #BANK SENERE
    elif(time==2):
        if(change=="EUR"):
            value=(value/9.1)*0.90
            end(value,change)
        if(change=="GBP"):
            value=(value/12.5)*0.90
            end(value,change)
        if(change=="RUB"):
            value=(value/0.15)*0.90
            end(value,change)

    #FLYPLASS NÅ
    elif(time==3):
        if(change=="EUR"):
            value=(value/9.1)*0.90
            end(value,change)
        if(change=="GBP"):
            value=(value/12.5)*0.90
            end(value,change)
        if(change=="RUB"):
            value=(value/0.15)*0.90
            end(value,change)
    #FLYPLASS SENERE
    elif(time==4):
        if(change=="EUR"):
            value=(value/9.1)*0.90
            end(value,change)
        if(change=="GBP"):
            value=(value/12.5)*0.90
            end(value,change)
        if(change=="RUB"):
            value=(value/0.15)*0.90
            end(value,change)
#Slutt sum
def end(value,change):
    print("Du mottok ",format(value ,".2f"),change,sep='')
    return 0

valuta()