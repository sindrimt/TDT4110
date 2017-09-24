"""

filnavn = input("Oppgi navn på fil")
f = open(filnavn,'w')
print("Skriv inn tekst som skal lagres i",filnavn)
print("Avslutt med å trykke på enter (uten tekst)")

tekst = "noe" #for å kjøre while-løkka
enter = "\n"

while tekst!="":
    tekst = input("> ")
    if (tekst != ""):
        f.write(tekst+enter)

f.close()

print("Filen har blitt lagret!")






filnavn = input("Oppgi navn på fil")
print("Skriv inn tekst som skal lagres i",filnavn)
print("Avslutt med å trykke på enter (uten tekst)")

tekst = "noe" #for å kjøre while-løkka
enter = "\n"
liste = []

while tekst!="":
    tekst = input("> ")
    if (tekst != ""):
        liste.append(tekst+enter)

f = open(filnavn,'w')
f.writelines(liste)

f.close()


print("Filen har blitt lagret!",filnavn)





filnavn = input("Oppgi navn på fil")
f = open(filnavn,'w')

print("Skriv inn positive tall, og tallet lagres i",filnavn)
print("Avslutt med å skrive -1")

tall = 0 #for å kjøre while-løkka
enter = "\n"

while tall!=-1:
    tall = int(input("> "))
    if (tall != -1):
        f.write(str(tall*tall)+enter)




f.close()


print("Filen har blitt lagret!",filnavn)




#les inn alt innhold til variabel
filnavn = input("Oppgi navn på fila:")
f = open(filnavn,"r")
innhold = f.read()
f.close()
print(innhold)

filnavn = input("Oppgi navn på fila:")
f = open(filnavn,"r")
teller = 1
linje = f.readline() #leser inn en linje fra fila

while (linje): #så lenge linje har innhold
    ren_linje = linje.strip() #fjerner linjeskift, etc.
    print(teller, "\t",ren_linje)
    linje = f.readline()
    teller += 1



f = open("test.txt","r")
print(f)
liste = f.readlines()
for i in range (10):

    print(i,liste [i].strip())




filnavn = input("Navn på fil:")
f = open(filnavn,"r")

for i in innhold:


    tall = int(i)
    print(tall**3)


"""
import time # For å lage tidsforsinkelse
import random #For å lage tilfeldig forsinkelse

import os

print(os.getcwd())

filnavn = input("Oppgi navn på fila:")
f = open(filnavn.strip(),"r") #Åpner fol for lesning

for x in range (40):
    print("")

tegn = f.read(1) #leser ett tegn fra fila
while (tegn):
    print(tegn,end="", flush=True) #skriver ut ett tegn uten linjeskift
    time.sleep(random.random()/5) #Random tidsforsinkelse
    tegn = f.read(1)

f.close()


"""
try: #her kommer kode som er litt usikker

    tall = int(input("Skriv inn et heltall"))
    print("500 delt på",tall,"er",500/tall)
    filnavn = input("Skriv inn navn på fil:")
    f = open(filnavn)
    test = f.read()
    f.close()
    print(test)

except ValueError:
    print("Må skrive heltall")

except ZeroDivisionError:
    print("Kan ikke dele på 0")

except IOError:
    print("Problemer med fillesing")

except:
    print("vet ikke helt hva som var feil")

#except Exception as variabel:
#else:
#finally:

"""