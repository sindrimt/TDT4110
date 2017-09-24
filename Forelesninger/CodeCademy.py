"""

# %s byttes ut med %(name)

#Eks1:

name = "Mike"
print( "Hello %s" % name)

#Eks2:

string_1 = "Camelot"
string_2 = "place"

print ("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))

################################################################################################

#Eks med dat og tid

from datetime import datetime

tid = datetime.now()

print("Tid:",tid)
print("År",tid.year)
print ("Måned:",tid.month)
print("Dag:",tid.day)
print("Dato:",tid.date())
print("Time:",tid.hour)
print("Miniutt:",tid.minute)
print("Sekunder:",tid. second)


print ('Dato: %s/%s/%s' % (tid.day, tid.month, tid.year))
print ('Klokken: %s:%s:%s' % (tid.hour, tid.minute, tid.second))
print ('%s/%s/%s %s:%s:%s' %(tid.month, tid.day, tid.year, tid.hour, tid.minute, tid.second))


################################################################################################

"""

