#James Roth
#2/26/18
#fri13th.py - printing the next 10 friday the 13ths

from calendar import weekday
from datetime import date
found=0
monthCount=date.today()month
yearCount=date.today()year

"""
date.today().day
date.today().month
date.today().year
weekday(year,month,day)
"""

while found<10:
    if date.today().day>13: #does this month have a fri 13th
        if monthCount<12: #is it december?
            monthCount+=1
        elif monthCount==12:
            monthCount=1
            yearcount+=1
    if weekday(yearCount,monthCount, 13) == 4: #if the 13th is friday
        found+=1
        print(yearCount, monthCount, 13)
    if monthCount<12:  #is it december?
            monthCount+=1
    elif monthCount==12:
            monthCount=1
            yearcount+=1