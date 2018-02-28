#James Roth
#2/28/18
#betterAdditionGameDemo.py - the name says it all

from random import randint

numCorrect=0
while numCorrect<5:
    num1=randint(-10,10)
    num2=randint(-10,10)
    answer=int(input("What is the sum of " + str(num1) + " and " + str(num2)))
    if answer==num1+num2:
        print("Correct!")
        numCorrect+=1
    
