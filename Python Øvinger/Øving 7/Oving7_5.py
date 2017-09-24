import math

def ducci(liste):
    print("Liste:             ",liste)

    lengde = (len(liste)-1)

    allerekker = []
    it = 0

    while liste not in allerekker or not sum(allerekker[-1])==0:
        allerekker.append(liste)
        rekke = []

        while len(rekke) < lengde:
            for i in range (lengde):
                rekke.append((math.fabs(liste[i]-liste[i+1])))
        rekke.append((math.fabs(liste[lengde]-liste[0])))

        liste = rekke
        it += 1
    print("Antall iterasjoner:",it+1,"\nSiste Ducci rekke: ",allerekker[-1])


liste=[10,8,1,15,5,7,43,21]
ducci(liste)

