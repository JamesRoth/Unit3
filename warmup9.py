#James Roth
#3/1/18
#warmup9.py - warm up

text=input("Enter some text: ")

string=""
for ch in text:
    if ch=="o" or ch=="i" or ch=="e" or ch=="a" or ch=="u":
        string=string+"ch.upper()"
    else:
        srting=string+"ch"
print(string)