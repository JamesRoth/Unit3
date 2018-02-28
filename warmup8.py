#James Roth
#2/28/18
#warmup8.py - sum of all numbers below 100,000 that are divisible by 3, 10, 17

total=0
for i in range(3, 100,001, 3):
    if i%10==0 and i%17==0:
        total+=i
    
