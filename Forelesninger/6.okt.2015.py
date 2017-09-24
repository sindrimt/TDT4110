"""
liste = [1,3,5,7,9]*5

for e in liste:
    print(e*e)
"""
"""
liste = [1,3,5,7,9]*5
lengde = len(liste)

for i in range(0,len(liste),3):
    print(liste[i]*liste[i])
"""
"""
A = [2,4,6,8,10,12,14,16,18,20]
i=0

#Bytter ut hver andre alement i liste A med tre-gangeren.
for x in range(1,len(A),2):
    i += 1
    A[x]=3*i
print(A)
"""

liste = [1,2,3,4,5,6]

x = liste [:2]
print(x)

liste [0:4]=[9,9,9]
print(liste)

liste = [1,2,3]

liste [3:]=[4,5,6]
print(liste)

liste = [1,2,3]
liste.extend([4,5,6,7,8])
print(liste)

print("Legger til 101,100 og 101 i liste")
liste = [1,2,3]
liste [2:2]=[101,100,101]
print(liste)

if 100 in liste:
    print("Sjekker om 100 er i listen. \nTrue")

print("Hvor i listen befinner 100 seg. Plassering: ")
print (liste.index(100))

print("Sletter 100 fra liste")
del liste [3]
print(liste)

print("Sorterer liste")
liste.sort()
print(liste)

print("Bytter rekkefølge")
liste.reverse()
print(liste)

print("Minimum i liste: ",min(liste),"Maks: ", max(liste))