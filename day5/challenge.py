# program to calculate lists of sudents' height
# student_heights = input("input a list of student heights ").split()
# for n in range(0,len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
# sum = 0
# for n in student_heights:
#     sum += n
#     div = sum / len(student_heights)
#     approximate = round(div)
# print(f"The average of the heights is {approximate }")
# challenge on maximum score
# student_scores = input("Input a list of student scores: ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)


# maximum_score = student_scores[0]
# for student_score in student_scores:
#     if student_score > maximum_score:
#         maximum_score = student_score
# print(f"The maximum score is: {maximum_score}")
# # program to add even number from 1 to 100
# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)
# # Another way 
# total2 = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total2 += number
# print(total2)

for number in range(1, 101):
    # print(number)
    if number % 3 == 0 and number % 5 == 0:
        print("fizzBuzz")
    elif number % 5== 0:
        print("Buzz")
    elif number % 3 == 0:
        print("fizz")
    else:
        print(number)

        
        
    
    