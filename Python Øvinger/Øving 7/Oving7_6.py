liste = [20,16,3,42,33,11,15,6,3,2]

#Sorterer liste fra minste til største tall
def bubbleSort(liste):
    print("Gammel liste:",liste)
    for i in range(len(liste)):
        for i in range (len(liste)-1):
            if liste [i] > liste[i+1]:
                temp = liste[i]
                liste[i] = liste [i+1]
                liste [i+1] = temp
    print("Ny liste:    ",liste)

print(bubbleSort(liste),"\n"*5)

print("\n")




liste2 = [20,16,3,42,33,11,15,6,3,2]

#Lager ny liste med største til minst

def selectionSort(liste):
    liste2 = []
    print("Gammel liste:",liste)
    lengde = (len(liste))
    while len(liste2) < lengde:
        liste2.insert(0,max(liste))
        liste.remove(max(liste))
    print("Ny liste:    ",liste2)
selectionSort(liste2)
