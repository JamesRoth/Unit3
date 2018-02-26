#James Roth
#2/26/18
#perfectNumber.py - does a number add up to its divisors

num=int(input("Enter an integer: "))
total=0
for i in range (1, num//2+1):
    if num%i==0:
        total=total+i
if total=num:
    print(num, "is a perfect number!")
else:
    print(num, "is not a perfect number.")