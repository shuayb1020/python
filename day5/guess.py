import random
start = int(input("Guess a number from 1 to 10: "))
# pick = random.randint(1,100)
# if start == pick:
#     print("You won")
# else:
#     print(f"You lose, the number is {pick}")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
select = random.randint(1, len(numbers))
if start == select:
        print("You won")
else:
    print(f"You lose, the number is {select}")


