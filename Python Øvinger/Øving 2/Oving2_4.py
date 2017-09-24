x = 2
y = input (’Skriv inn et tall ")
    z = x // y
print (z)
#I programmet ovenfor kalles y og x for?

#Svar: De kalles variabler. Det mangler " i input.

#Hva blir skrevet ut i koden nedenfor.

a = 2
b = 3
if (b<a or not b%a): #hvis b<a eller b modulo a gir en rest, utfør neste linje.
    b = a+b
else: #alt annet gi a en ny verdi. a*b
    a = a*b
print("a: ",a)
print("b: ",b)

#-------------------------------------------------------

#Hva gjør funksjone func1() og func2()? Gi disse funksjonene bedre navn. Kommenter funksjonene, og gi bedre variabelnavn der det trengs.


def func1(a):
    import random
    x = [0 for i in range(a)]

    for i in range(a):
        x[i] = random.randint(0,10)#intervall

    return x

def func2(x):
    return sorted(x)
# Dette er en kommentar
tall = int(input("Skriv inn et tall: "))
k = func1(tall)
y = func2(k)
print(y)
