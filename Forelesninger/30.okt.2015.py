"""
a = set(["Tekst",True,4,20])
b = set ([5,3,3,12])
print(b)
c = a.union(b)
a.add(4)
b.update([2,4,6,10])
c.remove (True)
print(c)
d = c.intersection(b)
print(d)





print('Dette programmet tester noen mengdeoperasjoner')
print('På hvert spørsmål, skriv inn navnet på noen personer')
print('med mellomrom mellom, f.eks. Ole Nina Per Anne')
print('Det bør være noen navn felles mellom listene og noen ulike')

streng_V = input('Hvem kan ha hatt tilgang til våpnet? ')
V = set(streng_V.split())
# Skriv en setning her som lager en mengde V av navn fra streng_V
# Hint: bruk funksjonene split() og set()

streng_M = input('Hvem hadde motiv for forbrytelsen? ')
# tilsvarende som over, lag en mengde M
M = set(streng_M.split())

streng_A = input('Hvem har alibi? ')
# tilsvarende som over, lag en mengde A
A = set(streng_A.split())

# beregn mengden av personer som både er i V og M men IKKE i A:
mistenkte = V.intersection(M).difference(A)

print('Mulige mistenkte kan være', mistenkte)


"""

def test():
    fjell_lister =  [['Jo', 'Ine', 'Eli', 'Bo', 'Ron', 'Sam', 'Una', 'Ron'],
                     ['Eli', 'Ada', 'Oda', 'Jo', 'Dag', 'Una', 'Ron'],
                     ['Bo', 'Ada', 'Tor', 'Dag', 'Jo', 'Eli', 'Frank']]
    print('Alle deltagere (minst ett fjell):', alle_delt(fjell_lister))
    n = len(fjell_lister)
    print('Vært på alle', n, 'fjell:', ivrigste_deltagere(fjell_lister))

def alle_delt(lister):
    # INPUT: en liste av lister, hvor hver indre liste inneholder navn
    #        på deltagere som har besøkt et visst punkt av interesse
    # PROS.: gjør om de indre listene til mengder og tar snittet av dem
    #        for å finne mengden av deltagere som har vært på minst ett sted
    # OUTPUT: returnerer mengden av deltagere som har vært på minst ett sted
    deltagermengde = set() # initialiserer til tom mengde
    for i in range(len(lister)):
        deltagermengde = deltagermengde.union(set(lister[i]))
    return deltagermengde

def ivrigste_deltagere(lister):
    # INPUT: en liste av lister, hvor hver indre liste inneholder navn
    #        på deltagere som har besøkt et visst punkt av interesse
    # PROS.: gjør om de indre listene til mengder og tar snittet av dem
    #        for å finne mengden av deltagere som har vært på alle stedene
    # OUTPUT: returnerer mengden av deltagere som har vært på alle stedene
    resultat = set(lister[0]) # initialiserer til mengden for første fjelltopp
    for i in range(1, len(lister)):
        resultat = resultat.intersection(set(lister[i]))

    return resultat

test()

