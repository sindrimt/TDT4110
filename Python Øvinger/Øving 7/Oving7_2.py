#Sjekker om liste "numbers" er større/mindre enn threshold. Deler numbers opp i nye lister.
def seperate (numbers,threshold):
    list_low =[]
    list_high = []
    for i in range(len(numbers)):
        if i < threshold-1:
            x = numbers [i]
            list_low.append(x)

        else:
            x = numbers [i]
            list_high.append(x)
    return list_low,list_high

print(seperate([10,11,12,13,14,15],12))

print("\n")

#Lager en matrise med lengde
def multiplication_table (n):
    matrix = []
    for x in range(1,n+1):
        matrix.append([x])
        for y in range (1,n+1):
            matrix[x-1].append(x*y)
    for a in range(0,n):
        del matrix[a][0]
    for i in range (len(matrix)):
        print(matrix[i])

multiplication_table(3)




