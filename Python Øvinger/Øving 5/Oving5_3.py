def is_leap_year (year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

def weekday_newyear (year):
    weekday = -1
    for i in range (1900,year+1):
        wasleap = is_leap_year(i-1)
        if wasleap:
            weekday += 2
        else:
            weekday += 1

    if weekday >6:
        weekday %= 7
    return weekday

def type_day (weekday):
    if weekday==0:
        return "man"
    elif weekday ==1:
        return "tir"
    elif weekday ==2:
        return "ons"
    elif weekday ==3:
        return "tor"
    elif weekday ==4:
        return "fre"
    elif weekday ==5:
        return "lør"
    elif weekday ==6:
        return "søn"

def is_workday(weekday):
    if weekday >= 5:
        return False
    else:
        return True

def workdays_in_year(year):
    workdays = []
    first_day = weekday_newyear(year)
    if is_leap_year(year):
        for i in range (first_day, first_day + 7):
            if i > 6:
                i %= 7
            if i > 4:
                workdays.append(0)
            else:
                workdays.append(1)
        work_year = workdays * 52

        last_day = first_day + 6
        if last_day > 6:
            last_day %= 7
        if last_day > 4:
            print(year,sum(work_year))
        else:
            work_year.append(1)
            print(year,sum(work_year))
    else:
        for i in range (first_day, first_day + 7):
            if i > 6:
                i %= 7
            if i > 4:
                workdays.append(0)
            else:
                workdays.append(1)
        work_year = sum(workdays) * 52
        print(year,work_year)







for i in range (1900, 1920):
    workdays_in_year(i)


FAAAAAN