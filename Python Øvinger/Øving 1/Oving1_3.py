count=1
def main():
    logg("23:59","Mr. Y",'"Har du mottatt pakken?"')
    logg("0:00","Mdm. Evil",'"Ja. Pakken er mottatt."')
    logg("0:03","Dr. Horrible",'"All you need is love!"')
    logg("0:09","Mr. Y",'"Dr. Horrible, Dr. Horrible , calling Dr. Horrible ."')
    logg("0:09","Mr. Y",'"Dr. Horrible, Dr. Horrible wake up now."')
    logg("0:09","Dr. Horrible",'"Up now!"')
def logg(tid,navn,melding):
    global count
    print("Msg",count,tid,"sendte ", navn,"følgende melding: ",melding)
    count+=1

main()
