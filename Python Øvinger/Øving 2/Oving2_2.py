print("en annengradsformel er gitt ved ax^2+bx+c.")
print("dette programmet sjekker hvor mange løsninger din ligning har og om de er imaginære eller ikke.")

a=float(input("Hva er din 'a'? "))
b=float(input("Hva er din 'b'? "))
c=float(input("Hva er din 'c'? "))
d=pow(b,2)-4*a*c

print("Din ligning var: ",a,"x^2 +",b,"x +",c)

if(d<0):
    print("Din ligning gir 2 løsninger og er et imaginært tall.")
elif(d>0):
    print("Din ligning gir 2 løsninger og er et reelt tall.")
else:
    print("Din ligning er lik 0 og gir en løsning.")