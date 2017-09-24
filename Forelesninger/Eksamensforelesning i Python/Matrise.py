matrix = []

for x in range(10):
    matrix.append([])
    for y in range(10):
        matrix[x].append((x+1)*(y+1))

#for rad in matrix:
    #print(rad)

s = ""

for rad in matrix:
    for tall in rad:
        s += "|".rjust(3) + str(tall).rjust(4)

    s += "\n"


print(s)