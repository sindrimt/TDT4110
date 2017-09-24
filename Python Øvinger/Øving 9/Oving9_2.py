#r=rente
#k=antal år
#A=sum invistert
#V=ønsket sluttsum
#n=antall terminer
def main ():
    V = float(input("Hva er ønsket sluttsum?"))
    r = 0.05
    k = 20
    n = 4
    verdi(r,k,V,n)

"""
def verdi (r,k,A,n):
    k_rente = []
    for i in range(k+1):
        value = A*((1+r/n))**(n*i)
        k_rente.append(round(value,2))

        print("År: ",k,"Verdi: ", round(value,2))

"""

def verdi (r,k,V,n):
    k_rente = []
    for i in range(k+1):
        A = V/(((1+r/n))**(n*i))
        k_rente.append(round(A,2))

    print("Du trenger å invistere minst: ",((A//1000+1)*1000),"kr \n", sep='')


main()



main()