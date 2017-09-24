"""
n = int(input("Skriv et antall. Der antall er n-iterasjoner"))
tot = 0
for i in range (1,n):
    x = 1/(i*i)
    tot += x

print (tot)
"""

tol = 0.000000001
x = 1
tot = 0
i = 0

def regne(tol,x,tot,i):
    while (x > tol):
        i += 1
        x = 1/(i*i)
        tot += x
    print("ca",format(tot,'.4f'))

regne(tol,x,tot,i)