"""
k = float(input("Skriv ett tall"))
count = 0
l = []

def utregning (k):
    global count
    global l
    count += 1
    if (k==0):
        l.append(0)
        return 0
    elif (k == 1):
        l.append(1)
        return 1
    else:
        l.append(utregning(k-1)+utregning(k-2))
        return utregning(k-1)+utregning(k-2)



print(utregning(k))
print('Gikk igjennom utregningen '+repr(count)+' ganger')
print(l)
"""


tall = int(input("Skriv inn tall: "))
"""
sett f1 = 0 og f2 = 1
lag liste
sett f1 = f2 og f2 = f1(gammel f1-verdi)+f2
putt f1 i liste
utfør "tall"-ganger
print fib. nr tall og sum av fib. fra 0-tall
"""
def fib(tall):
    f1,f2 = 0,1
    l = []
    for ape in range(tall):
        f1, f2 = f2, f1 + f2
        l.append(f1)
    print("Ditt fibonacci tall er: f(",tall,"):",f1,"\nListen er følgende: ",l,sep='')
    print("Summen av listen er: ",sum (l))

fib(tall)