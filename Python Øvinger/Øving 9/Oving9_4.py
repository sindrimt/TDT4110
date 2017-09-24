birthdays = {
"22 nov": ["Lars","Mathias"],
"10 des": ["Elle"],
"30 okt": ["Veronica","Rune"],
"12 jan": ["Silje"],
"31 okt": ["Willy"],
"8 jul": ["Brage","Øystein"],
"1 mar": ["Nina"],
}

def add_birthday_to_date(date,name):

    try:
        birthdays[date].append(name)
        print(name,"sin bursdag den",date,"er lagt til",)
    except KeyError:
        birthdays[date] = [name]
        print(name,"sin bursdag den",date,"er lagt til",)

add_birthday_to_date("29 okt","Gunnar")

for i in birthdays:
    print(i,birthdays[i])