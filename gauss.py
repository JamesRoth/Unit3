#James Roth
#2/15/18
#gauss.py - adding all numbers from 1-100

range1=int(input("What number would you like to start at: "))
range2=int(input("What number would you like to end at: "))
jump=int(input("How much would you like to jump up by: "))

total=0
for i in range(range1, range2+1, jump):
    total=total+i
