programming_dictionary = {
    "Bug":"An error in a program that prevents the program from running as expected.",
    "function": "A piece of code that you can easily call over again",
     "Loop": "The action of doing something over again"
    }
# retrieving information from dictionary
# print(programming_dictionary["Bug"])
# adding new item to a dictionary
programming_dictionary["variable"]= "The named storage of an item"

# wiping off an existing dcitionary
# programming_dictionary = {}
# print(programming_dictionary)

#Editing dictionary
programming_dictionary["variable"] = "it is a way of storing data value" 
# print(programming_dictionary)
# Looping through dictionary. this show only the keys 
for item in programming_dictionary:
    print(item)
# looping through dictionary and printing both key and value
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
    