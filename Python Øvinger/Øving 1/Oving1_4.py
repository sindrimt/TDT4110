import math
print("Velkommen til tetraeder-kalkulatoren.")
print("")
print("Her kan du få både arealet og volumet til tetraederet så lenge du har høyden.")
hight=int(input("Hva er høyden? (Høyden skal være i heltall)."))
a=3/math.sqrt(6)*hight
surface=math.sqrt(3)*pow(a,2)
print()
print("Overflaten til et tetraeder med høyde",hight,"er:",format(surface,'.3f' ))
#areal til teatraeder med høyde x
volum=math.sqrt(2)*pow(a,3)/12
print("Volumet til et tetraeder med høyde",hight,"er:",format(volum,'.3f'))
#volum til teatraeder med høyde x