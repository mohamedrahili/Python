# List of student grades, names, and IDs
grades = [85, 72, 90, 55, 68, 70, 45, 88, 92, 67]
student_ids = ['bj92393', 'bj92394', 'bj92395', 'bj92396', 'bj92397', 'bj92398', 'bj92399', 'bj92400', 'bj92401', 'bj92402']
student_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']

# Task 1: Calculate and print the average grades of all students
average_grade = sum(grades) / len(grades)
print(f"Average grade: {average_grade:.2f}")

# Task 2: Find and print the highest score and corresponding student ID number
highest_grade = max(grades)
highest_grade_id = grades.index(highest_grade)
print(f"The highest score is {highest_grade} for the student ID is {student_ids[highest_grade_id]} his name is {student_names[highest_grade_id]}")

# Task 3: Find and print the lowest score and corresponding student ID number
lowest_grade = min(grades)
lowest_grade_id = grades.index(lowest_grade)
print(f"The lowest score is {lowest_grade} for the student ID  {student_ids[lowest_grade_id]} his name is {student_names[lowest_grade_id]}")

# Task 4: Create a new list containing all students with grades >= 60 and print this list
passing_students = [(student_names[i], student_ids[i], grades[i]) for i in range(len(grades)) if grades[i] >= 60]
print(f"{len(passing_students)} students passe they are")
for student in passing_students:
    print(f"Name: {student[0]}, ID: {student[1]}, Grade: {student[2]}")

# Task 5: Count and print the number of students who failed (grades < 60)
failed_students = [(student_names[i], student_ids[i]) for i in range(len(grades)) if grades[i] < 60]
print(f"{len(failed_students)} students failed they are ")
for student in failed_students:
    print(f"Name: {student[0]}, ID: {student[1]}")
