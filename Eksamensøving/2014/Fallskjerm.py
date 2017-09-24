def inputPerson():
    liste = []
    name = input("Navn?")
    id = input("ID?")
    kg = int(input("KG?"))
    size = int(input("Size?"))
    liste = [name,id,kg,size]
    
    return liste

def readDbFile():
    
    with open('members.txt',"r") as file:
        liste = [line.strip().split(";") for line in file]
        
    return liste


def printMemberList():
    db = readDbFile()
    
    print(("NAME").ljust(15)+("ID-NR").ljust(9)+("VEKT").ljust(5)+("kg.").ljust(2)+("SIZE").rjust(7))
    
    for verdi in db:
        print((verdi[0]).ljust(15)+(verdi[1]).ljust(9)+(verdi[2]).ljust(5)+(verdi[3]).rjust(9))
printMemberList()

def addPerson ():
    person = inputPerson()
    with open ("members.txt","a") as file:
        file.write("\n"+person[0]+";"+person[1]+";"+str(person[2])+";"+str(person[3]))
    return readDbFile()
    
def feet2seconds(feet):
    if feet < 3000:
        return 0
    elif feet <=4000:
        seconds = (feet-3000)/100
        return seconds
    else:
        seconds = (feet-4000)/200 + 10
        return seconds