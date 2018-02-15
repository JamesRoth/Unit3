#James Roth
#2/15/18
#unitConverterUpdated.py - adding loops and breaks

convert=float(input("What would you like to convert? Enter 1 for KM to Miles, 2 for KG to LBS, 3 for Liters to Gallons, and 4 for Celsius to Fahrenheight."))
if convert==1:
    km=float(input("Enter amount of KM: "))
    print(km, "kilometers is", round(km*0.621371, 1), "miles.")
elif convert==2:
    kg=float(input("Enter a number of kilograms: "))
    print(kg, "kilograms is", kg*2.20462, "pounds.")
elif convert==3:
    liters=float(input("Enter a number of liters: "))
    print(liters, "liters is", liters*0.264172, "gallons.")
elif convert==4:
    celsius=float(input("Enter a temp in celsius: "))
    print(celsius, "celsius is", celsius*(9/5)+32, "degress fahrenheight.")
else:
    print("Error - incompatible number")
