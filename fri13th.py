#James Roth
#2/26/18
#fri13th.py - printing the next 10 friday the 13ths

from calendar import weekday
from datetime import date
found=0
monthCount=0
yearCount=0

"""
date.today().day
date.today().month
date.today().year
weekday(year,month,day)
"""

while found<10:
    if date.today().day>13:
        monthCount
    weekday(date.today().year+yearCount, date.today().month+monthCount, date.today().day)
    
    found=found+1