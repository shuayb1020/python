bill = 0

height = int(input("What is your height? "))
if height >= 120:
    age = int(input("What is your age? "))
    if age < 12:
        bill= 5
        print("child ticket is $5")
    elif age <= 18 :
        bill = 7
        print("Youth ticket is $7")
    elif age >=45 and age <= 55:
        print("Everything is gonna be okay, you get a free ride from us")
    else:
        bill= 12
        print("Adult ticket is $12")
    photo = input("Did you want a photo? Y or N ") 
    if photo == "Y":
        bill = bill + 3
    print(f"Your final bill is ${bill}")       
else:
    print("Sorry!, You have to grow taller to ride")