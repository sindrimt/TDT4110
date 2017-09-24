import csv
f = csv.reader(open("poenggrenser_2011.csv", 'r'))

def alle_sokere():
    teller = 0
    for row in f:
        if "Alle" in row[1]:
            teller += 1
    return teller
print("Studier som tokk inn alle søkere:",alle_sokere())


def gjennomsnitt():
    gjsnitt = 0
    teller = 1
    for row in f:
        if 'NTNU' in row[0] and not "Alle" in row[1]:
            gjsnitt += float(row[1])
            teller += 1
    return (round(gjsnitt/teller,2))

#print("Gjennomsnittet på NTNU var:",gjennomsnitt())

def opptak_low():
    minimum = 999
    grense = 0
    for row in f:
        if not "Alle" in row[1]:
            grense = float(row[1])
            if grense < minimum:
                minimum = grense
    return minimum
#print("Minste poenggrense var:",opptak_low())