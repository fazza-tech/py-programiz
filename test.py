#find average mark
def find_average_mark(marks):
    sum_of_avg_mark = sum(marks)
    total_subjects  = len(marks)
    average_mark = sum_of_avg_mark/total_subjects
    return average_mark


#find grade
def compute_grade(average_mark):
    if average_mark>=80:
        grade = "A"
    elif average_mark>= 60:
        grade = 'B'
    elif average_mark >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade



marks = [55,64,75,80,65]

average_mark = find_average_mark(marks)
print(f"Your average mark is:: {average_mark}")

grade = compute_grade(average_mark)
print("Your grade is:: ", grade)
    