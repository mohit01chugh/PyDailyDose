# Dictionary to store student scores
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Dictionary to store student grades based on scores
student_grades = {}
for key, values in student_scores.items():
    # Assign grades based on score ranges
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

# Print the dictionary of student grades
print(student_grades)