"""
def  gjennomsnittet (liste):
    summen = 0
    for item in liste:
        summen += item

    gjsnitt = summen / len(liste)
    return gjsnitt

liste = []
tall = -1

while (tall!=0):
    tall = float(input("Skriv inn flere tall, avslutt med 0"))
    if tall !=0:
        liste.append(tall)

snitt = gjennomsnittet(liste)
print("Gjennomsnittet er", snitt)

tabell_10*10=[[0 for col in range(10) for row in range (10)]#funk itsj
"""
#3x3 matrise med 0'er

"""
tabell =[[0 for x in range(3)]for y in range(3)]

tall = 2 #teller

for x in range(3):
    for y in range(3):
        tabell [x][y] = tall
        tall+= 2

print(tabell)
"""

"""
def telle_tegn (str,sjekk):
    antall = 0
    for karakter in str:
        if karakter ==sjekk:
            antall +=1
    return antall

tekst = ("Politiet har pågrepet og siktet ny mann etter overdosedrapssaken i Bergen")

tegn = input("Hvilket tegn vil du sjekke?")
antall = telle_tegn(tekst,tegn)

print("Teksten inneholdt",antall,"av tegnet",tegn)

"""

def skriv_tegn_indeks (tekst,tegn):
    for indeks in range(len(tekst)):
        if tekst[indeks] == tegn:
            print("Fant",tegn,"på indeks:",indeks)
tekst = "Politiet har pågrepet og siktet ny mann etter overdosedrapssaken i Bergen"

tegn = input("Hvilket tegn vil du sjekke for ?")

print(skriv_tegn_indeks(tekst, tegn))