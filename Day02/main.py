print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
total_people = float(input("How many people to split the bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

if tip_percentage > 1:
    total_payment = round((total_bill*(1 + tip_percentage/100))/(total_people), 2)
    print(f"Each person should pay {total_payment}")
else:
    total_payment = round((total_bill*(1 + tip_percentage))/(total_people), 2)
    print(f"Each person should pay {total_payment}")