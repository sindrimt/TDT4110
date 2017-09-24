def createTable (number,size):
    tabell = [[number for col in range(size)] for row in range(size)]

    return tabell

print(createTable(1,2))

tabell=[[1,1,1],[1,1,1]]

def fillTable(tabell):
    number = 2

    for rad in range(len(tabell)):
        for rekke in range(len(tabell[rad])):
            tabell[rad][rekke] = number
            number += 2
    return tabell

print(fillTable(tabell))

def printTable (tabell):
    for y in range(len(tabell)):
        s=''
        for x in range(len(tabell[y])):
            s += str(tabell[y][x]).center(5)

        print(s)

printTable(tabell)