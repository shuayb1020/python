import random

toss = random.randint(0,1)
if toss == 1:
    print("Head")
else:
    print("Tail")
# code challenge on list
names = input("Give me everybody's name separated by comma. ")
nameString = names.split(", ")

num_item = len(nameString)
pick = random.randint(0,num_item -1)
person_to_pay = nameString[pick]
print(f"the person who will pay the bill is {person_to_pay}")