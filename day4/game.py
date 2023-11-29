# programme to predict feelings

import random

# print("Welcome to mood checker")
# name = input("Enter Your name. ")
# mood = ["happy", "sad", "worried"]
# M = len(mood)
# selection = random.randint(0,M-1)
# prediction = mood[selection]
# print(f"Dear {name}, You are {prediction}")
# if selection == 0:
#     print("happiness is yours forever")
# elif selection == 1:
#     print("please try to be happy")
# else:
#     print("Do not worry much, all will be fine ")
    
letter = input("enter a letter ")
case =letter.isupper()    
if case == True:
    print("Its capital letter")
else:
    print("its a lowercase letter")
test = random.randint(0,64)
rest = random.randrange(0,20,2)
print(rest)