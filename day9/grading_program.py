student_score ={
    "Harry":81,
    "Ron": 78,
    "Hermiione":99,
    "Draco":74,
    "Neville":62,
}

student_grade ={}
for student in student_score:
    score = student_score[student]
    if score > 90:
        student_grade[student] = "Outstanding"
    elif score > 80:
        student_grade[student] = "Exceeds Expectation"
    elif score > 70:
        student_grade[student] = "Acceptable"
    else:
        student_grade[student] = "Fail"       
print(student_grade)
