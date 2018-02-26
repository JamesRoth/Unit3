#James Roth
#2/26/18
#numberGuessingGame.py - guessing a number

from random import randint
timesguessed=1
num=randint(1,100)
guess=int(input("Guess an integer between 1 and 100: "))

while guess!=num:
    print("Try again.")
    timesguessed+=




if num==guess:
    print("You got it! It took you", timesguessed, "tries.")
else:
    print("Try again.")
    
    
