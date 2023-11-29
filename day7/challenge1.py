import random
from hangman_logo import stages


# word_list = ["ardvark", "baboon", "camel"]
import hangman_words
word_list = hangman_words.words

chosen_word = random.choice(word_list)

lives = 6
display = [ ]
for letter in chosen_word:
    display.append("_")
# i = 0
# while not i >= len(chosen_word):
#     i += 1
# another way for while

end_of_game = False
while not end_of_game:
    
    guess = input("Guess a letter: ").lower()
    
    # for letter in chosen_word:
    #     if letter == guess:
    #         display.insert(len(letter),letter)
    # print(display)
    # another way to write the code 
    word_length = len(chosen_word)
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives-=1
        print(f"remaining life is: {lives}")
        if lives == 0:
            end_of_game = True
            print("You lose!")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game =True
        print("You won!")
    print(stages[lives])
