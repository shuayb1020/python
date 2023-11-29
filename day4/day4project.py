import random

print('ROCK, SCISSORS, PAPER')
choice =int (input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
selection =int(random.randint(0,2))
print(f"computer chose {selection}")
if choice >= 3:
    print("You typed an invalid number, You lose!")
elif choice == 0 and selection == 2:
    print("You won")
elif selection == 0 and choice == 2:
    print("You lose!")
    
elif selection > choice:
    print("You Lose") 
elif choice > selection:
    print("You won")
    
elif selection == choice:
    print("Its a draw")
    

# elif choice == 1 and selectio == 0:
#     print(f"You choose{choice}\n You won")
# elif choice == selection:
#     print(f" You choose {choice}\n You draw")
# else:
#     print("you lose")
    
    


