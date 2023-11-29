exam ={}

def compare(scores):
    high=0
    for score in scores:
        AggrScore = scores[score]
        if AggrScore > high:
            high = AggrScore
            winner = score
    print(f"The winner is {winner} with the total score of {high}")
        
        
end_of_program = False
while not end_of_program:
    name = input("what is your name? ")
    score = int(input("wha is your score? "))
    exam[name]=score
    quest = input("Any other student?. type 'yes or no': ")
    if quest == "no":
        end_of_program = True
        compare(exam)