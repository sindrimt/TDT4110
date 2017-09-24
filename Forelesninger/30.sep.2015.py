import random
l = []
#print(random.randint(1,100)

#print(random.randrange(1,20,2))

"""
for k in range (20):
    print(random.randrange(4,41,4))
"""

"""
def areal (h,b):
    svar = h * b
    return svar

print(areal (10,2))
"""

"""
#BMI kalkulator:
#eval gjør om "2" til int og "2.5" til float

v = eval(input("Angi vekt i kg: "))
h = eval(input("Angi høyde i meter: "))

def bmi(v,h):
    return v/h**2

print(bmi(v,h))
"""
"""
# sjekker om et tall er 3-gangern.
def tre_gangern(tall):
    if (tall%3==0):
        return True
    else:
        return False

tall = int(input("Skriv ett tall i 3-gangern: "))
if tre_gangern(tall):
    print("Riktig")
else:
    print("Feil")

#print(tre_gangern(21))

"""
"""
def navn():
    x = input("Fornavn?: ")
    y = input("Etternavn?")
    return x,y

x,y = navn()
print(x,y)
"""

# tar inn tall og gjør om til romertall
def romertall(n):
    if (n==0) : return ''
    elif (n==1): return "I"
    elif (n==2): return "II"
    elif (n==3): return "III"
    elif (n==4): return "IV"
    elif (n==5): return "V"
    elif (n==6): return "VI"
    elif (n==7): return "VII"
    elif (n==8): return "VIII"
    elif (n==8): return "IX"
    else: "Tallet er for stort eller for lite"

n = 0

while (n>=0):
    n = int(input("Skriv ett tall mellom 0 og 9:"))
    r = romertall(n)
    print("Romertall for",n,"er ",r)


