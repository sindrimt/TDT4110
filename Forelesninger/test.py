# rects.py
r1x1 = 0
r1y1 = 0
r1x2 = 0
r1y2 = 0

r2x1 = 0
r2y1 = 0
r2x2 = 0
r2y2 = 0

def intervalsOverlap(n1, n2, m1, m2):
    return not (n1 > m2 or n2 < m1)

def rectanglesOverlap():
    return intervalsOverlap(r1x1, r1x2, r2x1, r2x2) and intervalsOverlap(r1y1, r1y2, r2y1, r2y2)

def rectangle2String(x1, y1, x2, y2):
    return "(" + str(x1) + "," + str(y1) + ")" + "," + "(" + str(x2) + "," + str(y2) + ")"

def main():

    global r1x1,r1x2,r1y1,r1y2,r2x1,r2x2,r2y1,r2y2
    while (True):
        print("Rect1: " + rectangle2String(r1x1, r1y1, r1x2, r1y2))
        print("Rect2: " + rectangle2String(r2x1, r2y1, r2x2, r2y2))
        token = input(" > ")
        if token == "overlaps?":
            print(rectanglesOverlap())
        elif token == "exit":
            break
        else:
            pos = token.find("=")
            if pos >= 4:
                val = float(token[pos + 1 :])
                if token.startswith("r1x1"):
                    r1x1 = val
                elif token.startswith("r1y1"):
                    r1y1 = val
                elif token.startswith("r1x2"):
                    r1x2 = val
                elif token.startswith("r1y2"):
                    r1y2 = val
                elif token.startswith("r2x1"):
                    r2x1 = val
                elif token.startswith("r2y1"):
                    r2y1 = val
                elif token.startswith("r2x2"):
                    r2x2 = val
                elif token.startswith("r2y2"):
                    r2y2 = val


main()






















# %s byttes ut med %(name)

"""
name = "Mike"
print( "Hello %s" % name)

test  = str(5)

print(test)



def myst3(A,x):
    for r in range(0,len(A)):
        for c in range(0,len(A[0])):
            if (A[r][c]==x):
                return r*c
    return 0

print(myst3([[1,2,3],[4,5,6],[7,8,9]],8))



PAREN=['(','[','{',')',']','}']
def test(expression):
    parentheses_list = []
    for char in expression:
        if char in PAREN[:3]: # start-parenthesis found
        # put corresponding end-parenthesis in the back of the list
            parentheses_list.append(PAREN[PAREN.index(char)+3])
        elif char in PAREN[3:]: # end-parenthesis found
            if char != parentheses_list[-1]: # not matched start-parenthesis
                return False
            else:
                parentheses_list.pop()
    return parentheses_list==[]
def main():
    print('A:', test('{a+4*[b-2*(c+5)]/11}'))
    print('B:', test('{a+4*[b-2*(c+5])/11}'))
    print('C:', test('{a+4*[b-2*(c+5])/11}}')) #should give False
main()




[ [1, 1, 1],
  [1, 1, 1],
  [1, 1, 1] ]

"""

"""
n = 5
matrix = [[1 for x in range(n)]for y in range(n)]
teller = 0

for x in range(n):
    for y in range(n):
        matrix[x][y] = (x+2)*(y+1)


print(matrix)




def gangetabell(min, max):
    # tom liste vi legger til radene i
    ans = []
    for i in range(min, max+1):
        temp = [] # midlertidig liste som vi bruker til mellomlagring
        for j in range(min, max+1):
            temp.append(i*j)
        ans.append(temp)

    for rekke in ans:
        print(rekke)
    return ans


gangetabell(1,5)

"""

