#input, ny liste, setter tall=1
l,tall,n = [],1,int(input("Skriv inn ett tall: "))

"""
sjekker om tall er oddetall eller partall
hvis partall: tall**2
hvis oddetall: tall*2 og bytt fortegn (*-1)
legg til +1 på tall
legg i liste
fortsett n ganger
"""

for k in range(n):
    if k%2==0:
        x = pow(tall,2)
    else:
        x = pow(tall,2)*(-1)
    tall += 1
    l.append(x)
print("Listen av tall er: ,",l,"Summen av tallene er: ",sum(l))
