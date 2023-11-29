print("Welcome to the tip calculator.")
totalBill=float(input("What was the total bill? $"))
tipPercent = int(input("what percentage tip would you like to give? 10, 12, or 15"))
people=int(input("How many people to split the bill? "))
perc = tipPercent/100 * totalBill
add = float(perc) + totalBill
payment = float(add)/people
Rpayment = round(payment,2)
print(f"Each person should pay: ${Rpayment}")