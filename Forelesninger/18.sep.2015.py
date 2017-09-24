



"""
for y in range (1,4):
    for x in range (1,4):
        z = x*y
        print(z)
"""


"""
for t in range (24):
    for m in range (60):
        for s in range(60):
            print(t,":",m,":",s)

"""

"""
for x in range (3,31,3):
    print(x,"\t",pow(x,2))
"""

"""n = 0
t = 0
for n in range(3,31):
    n = pow(t,3)
    t += 1
    print(n,"\t")
"""

"""
import random

x = random.randint(1,100)
y = -1

while (x!=y):
    y = int(input("Gjett ett heltall mellom 1-100 \n"))

    if(y==42):
        print("The answer of everything")
        break

    elif(y<x):
        print("Du skrev", y)
        print("Ditt tall er lavere enn skjult tall")
        print("Prøv igjen. \n")

    elif (y>x):
        print("Du skrev", y)
        print("Ditt tall er høyere enn skjult tall")
        print("Prøv igjen. \n")


    else:
        print("RIKTIG!")



print(x)
"""
"""
n = 5

while(n >0):
    print("Tallet ditt er nå",n)
    n -= 1


"""


"""

summen = 0
tall = 1
print("Skriv inn 0 for å avslutte")

while(tall !=0):
    tall = int(input("skriv inn et tall"))
    summen = summen + tall

print("summen er", summen)

"""