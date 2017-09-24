def mshd2s(min,sek,hundr):
    min *=60
    hundr = float(round((hundr/100),2))
    totalt = min+hundr+sek
    return (totalt)

def rundeTid (startTid,sluttTid):
    startTid = mshd2s(startTid[0],startTid[1],startTid[2])
    sluttTid = mshd2s(sluttTid[0],sluttTid[1],sluttTid[2])
    return round((sluttTid-startTid),2)

def alleRundeTider (passeringsTider):
    liste = []
    for i in range(0,len(passeringsTider)-1):
        startTid = passeringsTider[i]
        sluttTid = passeringsTider[i+1]
        liste.append(rundeTid(startTid,sluttTid))
    return liste

#alleRundeTider([[0,20,0],[0,50,10],[1,21,21],[1,53,33]])

pulsData = [110,118,125,127,127,130,129,131,132,134,134,135,145,157,165,172,173,178,179,178]

def pulsStatistikk(pulsData):
    snitt = 0
    maks = pulsData[0]
    minimum = pulsData[0]
    for x in pulsData:
        snitt += x
        if x < minimum:
            minimum = x
        if x > maks:
            maks = x

    return [(snitt/len(pulsData)),minimum,maks]

#print(pulsStatistikk(pulsData))

def pulsSoneGrense(maksPuls):
    oneP = maksPuls/100

    return [(round(oneP*60,2)),(round(oneP*72.5,2)),(round(oneP*82.5,2)),(round(oneP*87.5,2)),(round(oneP*92.5,2))]

#print(pulsSoneGrense(188))

def pulsSoner(maksPuls,pulsData):
    pulsGrense = pulsSoneGrense(maksPuls)
    sone1,sone2,sone3,sone4,sone5=0,0,0,0,0

    for puls in pulsData:

        if (puls >= pulsGrense[0]) and (puls < pulsGrense[1]):
            sone1 += 1

        elif (puls >= pulsGrense[1]) and (puls < pulsGrense[2]):
            sone2 += 1

        elif (puls >= pulsGrense[2]) and (puls < pulsGrense[3]):
            sone3 += 1

        elif (puls >= pulsGrense[3]) and (puls < pulsGrense[4]):
            sone4 += 1

        elif (puls >= pulsGrense[4]):
            sone5 += 1

    antall = len(pulsData)
    sone1=round((sone1/antall)*100,2)
    sone2=round((sone2/antall)*100,2)
    sone3=round((sone3/antall)*100,2)
    sone4=round((sone4/antall)*100,2)
    sone5=round((sone5/antall)*100,2)
    return [sone1,sone2,sone3,sone3,sone4,sone5]

#print(pulsSoner(188,pulsData))

def lengstePulsOkning(pulsData):
    posisjon = 0
    lengde = 0
    temp = 0
    p_teller = 0
    for i in range (0,len(pulsData)-1):

        if pulsData[i+1] >= pulsData[i]:
            temp += 1


        elif pulsData[i+1] < pulsData[i]:
            if temp > lengde:
                lengde = temp +1
                posisjon = p_teller
            p_teller = i+2
            temp = 0
            print(posisjon)
            print(pulsData[i+1],">",pulsData[i])

    return [lengde,posisjon]

#lengstePulsOkning(pulsData)

#[110,118,125,127,127,130,129,131,132,134,134,135,145,157,165,172,173,178,179,178]