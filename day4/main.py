import random

# random_integer = random.randint(1, 10)
# print(random_integer)
# # creating random floating point number
# random_float = random.random()
# print(random_float)
# # using random generator to calculate love score
# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")
# concept of list
# state_of_america =["Delaware", "Pennsylvania","New Jerswy", "Georgia", "Connecticut", ]
# print(state_of_america[0])

# index error and nested list
# dirty_dozen = ["strawberries", "spinach", "kale","nectaries","apple", "grapes", "peaches", "cherries", "pears", "tomatoes", "celery", "potatoes"]

fruits = ["strawberries","nectarines","apple", "grapes","peaches","cherries", "pears"]
vegetables = ["spinach","kale", "tomatoes", "celery", "potatoes"]
dirty_dozen=[fruits, vegetables]
print(dirty_dozen)
row1= [" ", " ", " "]
row2= [" ", " ", " "]
row3= [" ", " ", " "]
map =[row1, row2, row3]
print(f"1 {row1}\n2 {row2}\n3 {row3}")
position = input("where do you want to place the treasure? ")
horizontal = int(position[1])
vertical = int(position[0])
selected_row = map[vertical-1]
selected_row[horizontal-1] = "X"
print(map)
print(f"{row1}\n{row2}\n{row3}") 
