import random
names = ["Alex", "Beth", "Dave"]
student_score = {
    "Alex" : 90,
    "Beth" : 80,
    "Dave" : 56
}

student_scores = {student:student_score for student in names}
# print(student_scores)

passed_students = {student:score for (student,score) in student_score.items() if score >= 60}
print(passed_students)