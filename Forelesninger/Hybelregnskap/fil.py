# Modul fil - filfunksjoner

import pickle #Lagerer dictioary/filer rett til disk

def save (db,filnavn):
    f = open(filnavn,'bw') #Åpner fil for skriving bin@rt
    pickle.dump(db,f) #Dumper innhold i dictionary til fil
    f.close()

def load (filnavn):
    f = open(filnavn,'br') #Åpner for lesing, binært
    db = pickle.load(f)
    f.close()
    return db
