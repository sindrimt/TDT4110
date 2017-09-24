fornavn = [
'johan', 'eli', 'mats', 'lene', 'simon',
'inger', 'henrik', 'mari', 'per']

etternavn = [
'Hag', 'Hag', 'Basmestad', 'Grimlavaag', 'Kleivesund',
'Fintenes', 'Svalesand', 'Molteby', 'Hegesen']


#printer liste 1 og 2 fra 0 til lengden av antal str i listen
for n in range(len(fornavn)):
    print(fornavn[n].capitalize(), etternavn[n])

print("\n")


etternavn2 = []

#lager en ny liste for "etternavn" baklengs [::-1]
for n in (etternavn)[::-1]:
    etternavn2.append(n)
#printer liste med fornavn + etternavn2
for n in range(len(fornavn)):
    print(fornavn[n].capitalize(), etternavn2[n])

"""
for f,n in zip(fornavn,etternavn2):
    print(f, n)
"""