#James Roth
#2/26/18
#divisors.py - entering a number and priting its divisors

num=int(input("Enter an interger: "))

for i in range (1, num/2+1):
    if num%i==0:
        print(i)
    
