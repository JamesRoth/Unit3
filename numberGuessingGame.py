#James Roth
#2/26/18
#numberGuessingGame.py - guessing a number

from random import randint
timesguessed=0
num=randint(1,100)
guess=int(input("Guess an integer between 1 and 100: "))

while guess!=num:
    print("Try again. You've tried", timesguessed+1, "times.")
    timesguessed+=1
    guess=int(input("Guess again: "))
print("You got it! It took you", timesguessed+1, "tries.")
