#James Roth
#2/26/18
#numberGuessingGame.py - guessing a number

from random import randint
timesguessed=0
num=randint(1,100)
guess=int(input("Guess an integer between 1 and 100: "))

while guess!=num:
    timesguessed+=1
    if guess<num:
        print("Too low.")
    else:
        print("Too high.")
    print("Try again. You've tried", timesguessed, "times.")
    guess=int(input("Guess again: "))
print("You got it! It took you", timesguessed+1, "tries.")
