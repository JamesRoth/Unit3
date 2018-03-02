#James Roth
#3/2/18
#changeComputerLoop.py - finding change w/ loops

money=int(input("Input a number of cents: "))
quaters=0
dimes=0
nickels=0
pennies=0

while money-25>=0:
    quaters+=1
    money-=25
while money-10>=0:
    dimes+=1
    money-=10
while money-5>=0:
    nickels+=1
    money-=5
while money-1>=0:
    pennies+=1
    money-=1
print(quaters, dimes, nickels, pennies)