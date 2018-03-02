#James Roth
#2/26/18
#fri13th.py - printing the next 10 friday the 13ths

from calendar import weekday
from datetime import date
found=0
monthCount=date.today().month
yearCount=date.today().year

if date.today().day>13: #does current month have a fri 13th
    if monthCount<12: #is it december?
            monthCount+=1
    else:
            monthCount=1
            yearcount+=1

while found<500:
    if weekday(yearCount,monthCount, 13) == 4: #if the 13th is friday
        found+=1
        print(monthCount, "/", 13, "/", yearCount)
    if monthCount<12:  #is it december?
        monthCount+=1
    else:
        monthCount=1
        yearCount+=1