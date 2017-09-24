li = [1,2,3,4,5,6]
def odde():
    for a in range(len(li)):
        if li[a] % 2 != 0:
            li[a] *= (-1)

    print(li)
    li.sort()
    li.reverse()
    print(li)

odde()

