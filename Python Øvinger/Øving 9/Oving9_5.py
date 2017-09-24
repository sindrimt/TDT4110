def number_of_lines(filename):
    return len(open(filename,'r').readlines())


#print(number_of_lines("numbers.txt"))

def number_frequency(filename):
    file = open(filename,'r').read().split('\n')
    dic = {}
    for tall in file:
        try:
            dic[int(tall)] += 1
        except KeyError:
            dic[int(tall)] =  1
    for i in dic:
        print(i,":",dic[i], sep='')

number_frequency("numbers.txt")