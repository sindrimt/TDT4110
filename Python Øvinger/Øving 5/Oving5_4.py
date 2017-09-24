alder = int(input("Hva er din alder? \n"))
if alder < 5:
    print("Småbarn")
    print("Gratis")
elif alder >=5 and alder <=20:
    print("Barn")
    print("20kr")
elif alder >=21 and alder <=25:
    print("Student")
    print("50kr")
elif alder >=26 and alder <=60:
    print("Voksen")
    print("80kr")
else:
    print("Honør")
    print("Gratis")

44