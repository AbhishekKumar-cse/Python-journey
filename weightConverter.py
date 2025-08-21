weight = int(input("Enter weight :"))
unit = input("Enter unit (kg/lb):")
if unit == "L" or unit == "l":
    converted=weight*0.45
    print(f"You are {converted} kilos")
elif unit == "K" or unit == "k":
    converted=weight*2.2
    print(f"You are {converted} pounds")
else:
    print("Invalid unit. Please enter 'kg' or 'lb'.")