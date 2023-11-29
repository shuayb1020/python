# number challenge
# two_digit_number =input("type two numbers: ")
# first_number = two_digit_number[0]
# second_number = two_digit_number[1]
# result = int(first_number) + int(second_number)
# print(result)
# challenge on BMI calculator
# height = float(input("enter your height in meter: "))
# weight = float(input("enter your weight in kg: "))
# height2 =float(height**2) 
# BMI =int(weight/height2) 
# print("your BMI is " + str(BMI)) 
# age challenge

age= input("what is your age? ")
totalDays =90* 365
totalMonth= 90*12
totalWeeks=90*52
currentWeek=int(age)*52
currentMonths= int(age)*12
currentDays=int(age)  *365
RemWeek = int(totalWeeks) - int(currentWeek)
RemMonths = int(totalMonth) - int(currentMonths)
RemDays = int(totalDays) - int(currentDays)
print(f"you have {RemDays} days, {RemWeek} weeks and {RemMonths} months")
