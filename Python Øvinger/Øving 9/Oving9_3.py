cheeses = {
'cheddar':
('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),

'mozarella':
('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),

'gombost':
('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),

'geitost':
('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),

'port salut':
('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),

'camembert':
('A243-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),

'ridder':
('GOMBOS-4', 'B16-3'),
}



infisert = {'A234','A235','B13','B14','B15','C31'}



for ost in cheeses:
    hyller = set()
    for hylleplass in cheeses[ost]:
        hylle = hylleplass.split('-')
        del hylle[1]
        hyller.update(hylle)
        hylle_inf = hyller.intersection(infisert)
        hylle_fri = hyller.union(hylle_inf)

    if hyller.intersection(infisert) != set():
        print("Infisert ost: ",ost,"/ Hylleplass: ",hylle_inf)

    elif hyller.intersection(infisert) == set():
        print("Ikke infisert: ",ost,"/ Hylleplass: ",hylle_fri)

