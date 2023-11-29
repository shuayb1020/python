number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print(str(number)+" is an even number.")
else:
    print(str(number)+" is an odd number.")
    
# # bmi calculation with interpretation
height = float(input("enter your height in meter: "))
weight = float(input("enter your weight in kg: "))
height2 =float(height**2) 
BMI =round(float(weight/height2)) 

print("your BMI is " + str(BMI))
if BMI < 18.5:
    print("You are underweight")
elif BMI < 25:
    print("you have normal weight")
elif BMI < 30:
    print(" You are overweight")
elif BMI < 35:
    print("you are obese")
else: 
    print("you are clinically obese") 
# challenge on leap year
year = int(input("What year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")    
else:
    print("not a leap year")    
# pizza ordering
bill = 0
print("Welcome to Python pizza deliveries!")
size = input("What size of pizza do you want? S, M, or L. ")
if size == "S":
    bill = 15
    print("small size is $15.")
elif size == "M":
    bill = 20
    print("Medium size is $20")
elif size == "L":
    bill = 25
    print("large size is $25")
else:
    print("choose from the three options, S, M, L")
add_pepperoni = input("Do you want pepperoni? Y or N. ")
extra_cheese = input("Do you want extra cheese? Y or N. ")

if add_pepperoni == "Y":
    bill += 2
if extra_cheese == "Y":
    bill +=1
print(f"your total bill is ${bill}")
# challenge on love calculator
name1= input("What is your name? \n")
name2 = input("What is their name? \n")
combinedString= name1 + name2
lower_case_string = combinedString.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e
l = lower_case_string.count("l")
o = lower_case_string.count("o")    
v = lower_case_string.count("v") 
e = lower_case_string.count("e")    
love = l + o + v + e 
love_score = int(str(true) + str(love))
# int_score = int(love_score)
if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, you go togther like coke and mentos")
elif love_score >= 40 and love_score <=50:
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(love_score)

    