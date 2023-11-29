
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i' ,'j', 
           'k', 'l', 'm', 'n', 'o','p', 'q','r', 's', 't', 'u', 'v', 'x',
           'y','z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
           'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers= ['0', '1', '2', '3', '4', '5', '6', '7','8','9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*','+']

print("Welcome to the PyPassword Generator!")
no_letters = int(input("How many Letters do you want ?\n"))
no_symbols = int(input("How many symbols do you want ?\n"))
no_numbers = int(input("How many numbers do you want ?\n"))

# Easy level

password = ""

for char in range(1,no_letters + 1):
    random_char = random.choice(letters)
    password += random_char
for sym in range(1, no_symbols + 1):
    random_sym = random.choice(symbols)
    password += random_sym
for num in range(1, no_numbers + 1):
    random_num = random.choice(numbers)
    password +=  random_num
print(password )

# Hard level
password_list = []

for char in range(1,no_letters + 1):
    random_char = random.choice(letters)
    password_list += random_char
for sym in range(1, no_symbols + 1):
    random_sym = random.choice(symbols)
    password_list += random_sym
for num in range(1, no_numbers + 1):
    random_num = random.choice(numbers)
    password_list +=  random_num
print(password_list )
random.shuffle(password_list)
print(password_list )
# changing list to string
password =""
for char in password_list:
    password += char
print(f"Your password is: {password}")


    

