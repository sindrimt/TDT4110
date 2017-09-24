def les():
    f = open ("BIBLE.txt").read()
    return f

print(ord(' '),ord(' '))


def rydd():
    f = les()
    a =''
    for bokstav in f:
        if not bokstav.lower()<chr(96) and not bokstav.lower()>chr(123) or bokstav.lower()==chr(32):
            a += bokstav
    print(a)
rydd()