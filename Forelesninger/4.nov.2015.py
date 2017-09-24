"""

import random

dict = {}
dict2 = {"fire":4,"fem":5}

dict['en'] = 1
dict['to'] = 2
dict['tre'] = 3

print(dict,dict2)

dict.update(dict2)
print(dict,"\n")


for key,value in dict.items():
    print("Nøkkel:",key+",","verdi:",value)

for key in dict:
    dict[key] += 1

print(dict)


dict['to tall'] = random.randint(1,5)
dict['to tall'] = dict['to tall'], random.randint(1,5)
print(dict)
"""
import random
mitt_sett = set()
for i in range(10):
    mitt_sett.add(random.randint(1,10))



print(mitt_sett)
