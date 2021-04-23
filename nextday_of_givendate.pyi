year = int(input("Enter a year: "))

if year % 400 == 0:
    leap = True
elif year % 100 == 0:
    leap = False
elif year % 4 == 0:
    leap = True
else:
    leap = False

month = int(input("Enter a month form 1 to 12: "))

if month in (1,3,5,7,8,10,12) :
    month_len = 31
elif month == 2:
    if leap:
        month_len = 29
    else:
        month_len = 28
else:
    month_len = 30

day = int(input("Enter a day from 1 to 31: "))

if day < month_len:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year +=1
    else:
        month += 1
print("The next date from the given date is %d-%d-%d.[yyyy-mm-dd] " % (year, month, day))



