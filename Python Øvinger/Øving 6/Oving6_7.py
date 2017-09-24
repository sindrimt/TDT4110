def getCoints():
    l_mynter = []
    mynter = -1
    while mynter != 0:
        mynter = int(input("Hva er summen av myntene dine?"))
        l_mynter.append(mynter)
    del l_mynter[-1]
    print("Du skrev inn følgende: ",l_mynter)
    numCoins(l_mynter)



def numCoins(l_mynter):
    coins = [0,0,0,0]
    for i in range(len(l_mynter)):
        if l_mynter[i] // 20:
            coins [0] = l_mynter[i] // 20
            l_mynter[i] %= 20

        if l_mynter[i] // 10:
            coins [1] = l_mynter[i] // 10
            l_mynter[i] %= 10

        if l_mynter[i] // 5:
            coins [2] = l_mynter[i] // 5
            l_mynter[i] %= 5

        if l_mynter[i] // 1:
            coins [3] = l_mynter[i] // 1
            l_mynter[i] %= 1
    print(coins[0],"stk 20kr, ",coins[1],"stk 10kr, ", coins[2],"stk 5kr, ",coins[3],"stk 1kr, \n", sep='')
    getCoints()

getCoints()