print("Welcome to Treasure Island!")
direction = input('where do you want to go? type "left" or "right" ').lower()

if direction == "left":
    action = input('What did you want to do? type "swim" or "wait"' )
    
    if action == "wait":
        door = input('Which door do you want to take? type "red", "blue" or "yellow" ')
        if door == "Y":
            print("Congratulations, You won the game!")
        else:
            print("Oops You took the wrong door!")    
    else:
        print("Sorry!, You took the wrong decisiom!.")        
else:
    print("Oops! Game Over!")         