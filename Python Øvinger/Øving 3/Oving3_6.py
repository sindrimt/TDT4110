debug = True

def mult():
    x = int(input("Skriv inn et tall: "))
    y = int(input("Skriv inn enda et tall: "))
    print(x*y)

    if debug== True:
        print("Tallene du skrev inn :",x,"og",y)

mult()