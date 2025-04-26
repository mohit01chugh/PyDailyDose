student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for key, values in student_scores.items():
    if values > 91:
        grades = "Outstanding"
        student_grades[key] = grades
    elif values > 81 and values < 90:
        grades = "Exceeds Expectations"
        student_grades[key] = grades
    elif values > 71 and values < 80:
        grades = "Acceptable"
        student_grades[key] = grades
    else:
        grades = "Fail"
        student_grades[key] = grades
print(student_grades)