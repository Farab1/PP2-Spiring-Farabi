import math
 
day=int(input('input day: ')) #14.07.2007
month=int(input('input month: '))
year=int(input('input year: '))

resultday=day
resultmonth= month
resultyear=year

if day>31 or month > 12 :
    print("impossible date")
    exit()
elif  month in [4, 6, 9, 11] and day > 30:
    print("impossible date")
    exit()
elif month == 2 and day>29:
    print("impossible date")
    exit()
elif year%4==0 and year%100!=0 and month ==2 and day>28 or year%400==0 and month ==2 and day>28:
    print("impossible date")
    exit()


if  day>5:
    resultday = day-5
    resultmonth = month
    resultyear=year
elif day<=5:
    if month == 1:
        resultday = 31-(5-day) 
        resultmonth = 12   
        resultyear = year-1
    elif month == 5 or 6 or 7 or 10 or 12:
        resultday = 30-(5-day) 
        resultmonth = month - 1
    elif year%4==0 and year%100!=0 and month ==3  or year%400==0 and month == 3:
        resultday = 28-(5-day)
        resulthmonth = month -1
    elif month == 2 or 4 or 8 or 11 or 9:
        resultday = 31-(5-day) 
        resultmonth=month -1

print('Result: ',resultday,resultmonth,resultyear)