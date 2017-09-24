weatherData = [[12.0, 2.4, 8.2],[6.1, 0.6, 11.9],[8.3, -3.5, 0.0],[11.6, -5.2, 0.0],[15.3, 2.8, 14.3]]

def weatherStats(weatherData):
    total_days = len(weatherData)
    total_rain = 0
    days = 0
    low = 999
    high = -999

    for day in weatherData:
        days += 1


        if day[0] > high:
            high = day[0]
            high_day = days

        if day[1]<low:
            low = day[1]
            low_day = days
        total_rain += day[2]

        
    print ('There are',str(total_days)+"days in the period.")
    print ('The highest temerature was',str(high)+"C on day number",high_day)
    print ('The lowest temerature was',str(low)+"C on day number", low_day)
    print ('There was a total of',round(total_rain,2),"mm rain in the period")


def coldestThreeDays (weatherData):
    min_temp = []
    average = 999
    for day in weatherData:
        min_temp.append(day[1])
    for day in range(0,len(min_temp)-2):
        
        temp_average = min_temp[day]+min_temp[day+1]+min_temp[day+2]
        
        if temp_average<average:
            average = temp_average

    return day


def addNewDay(extraData, weatherData):
    liste=[]
    liste = extraData.split()
    max_temp = float(liste[0][4:-1])
    min_temp = float(liste[1][4:-1])
    rain = float(liste[2][:-2])


    return weatherData

addNewDay('max=23.5, min=9.3, 5.1mm',weatherData)

