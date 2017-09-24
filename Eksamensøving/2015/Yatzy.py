import random

def throw(n):
    dice = []
    for i in range (0,n):
        dice.append(random.randint(1,6))
    return dice




def chance (dice):
    summen = 0
    for i in range(0,len(dice)):
        summen = dice[i]+summen
    return summen




dice=[2,3,4,5,6]

def house (dice):
    dice.sort()

    if (dice[0]!=dice[4]) and ((dice[0]==dice[1]) and (dice[2]==dice[3]==dice[3]==dice[4]) or (dice[0]==dice[1]==dice[1]==dice[2]) and (dice[3]==dice[4])):
        print(chance(dice))
        return 1
    else:
        return 0


def straight (dice):
    if dice == [1,2,3,4,5]:
        return 15
    if dice == [2,3,4,5,6]:
        return 20
    else:
        return 0
