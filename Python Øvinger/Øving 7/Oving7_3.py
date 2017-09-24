#Sjekker om sting 1 er lik string 2
def check (str1,str2):
    for i in range(len(str1)):
        if str1.lower()[i] != str2.lower()[i]:
            return False
    return True

print("Er tegnene like i str1 og str2?:", check("Test","Test"))


#Skriver string 1 baklengs
def reverse (str1):
    a = ""
    for c in str1[::-1]:
        a = a+c
    return a

print ("Revasjert:",reverse("Hei på deg!"))


#Sjekker om string 1 og 2 er palindrom
def palindrom (str1,str2):
    a = ""
    for i in str1.lower()[::-1]:
        a = a+i
    if a == str2.lower():
        return True
    else:
        return False

print(palindrom("Agnes i senga","Agnes i senga"))

#Sjekker om string 1 er inneholdt i string 2
def delmengde (str1,str2):
    if str1.lower() in str2.lower():
        return True
    else:
        return False

print("Er str1 i str2?:",delmengde("Hei","hei på deg"))


