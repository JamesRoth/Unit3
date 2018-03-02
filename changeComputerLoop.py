#James Roth
#3/2/18
#changeComputerLoop.py - finding change w/ loops

money=int(input("Input a number of cents: "))
quaters=0
dimes=0
nickels=0
pennies=0

while money-25>0:
    quaters+=1
