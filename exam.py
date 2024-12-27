import os  

students = []

def add_student():
    """Adds a new student to the system."""
    print("\n--- Add Student ---")
    first_name = input("Enter student's first name: ").strip()
    last_name = input("Enter student's last name: ").strip()
    student_id = input("Enter student ID: ").strip()
    filiere = input("Enter student's filière (field of study): ").strip()
    matiere = input("Enter subject for grade: ").strip()
    grade = input("Enter grade: ").strip()

    if not grade.isdigit():
        print("Invalid grade. Grade must be numeric.")
        return

    students.append({
        "first_name": first_name,
        "last_name": last_name,
        "id": student_id,
        "filiere": filiere,
        "matiere": matiere,
        "grade": int(grade)
    })
    print(f"Student {first_name} {last_name} added successfully!\n")

def view_students():
    """Displays all student records."""
    print("\n--- View Students ---")
    if not students:
        print("No students found.\n")
        return

    for i, student in enumerate(students, start=1):
        print(f"{i}. ID: {student['id']}, Name: {student['first_name']} {student['last_name']}, Filière: {student['filiere']}, Subject: {student['matiere']}, Grade: {student['grade']}")
    print()

def search_student():
    """Searches for a student by ID."""
    print("\n--- Search Student ---")
    search_id = input("Enter the ID of the student to search for: ").strip()
    found = False

    for student in students:
        if student['id'] == search_id:
            print(f"Found: ID: {student['id']}, Name: {student['first_name']} {student['last_name']}, Filière: {student['filiere']}, Subject: {student['matiere']}, Grade: {student['grade']}\n")
            found = True
            break

    if not found:
        print("Student not found.\n")

def delete_student():
    """Deletes a student by ID."""
    print("\n--- Delete Student ---")
    delete_id = input("Enter the ID of the student to delete: ").strip()

    for i, student in enumerate(students):
        if student['id'] == delete_id:
            del students[i]
            print(f"Student with ID {delete_id} deleted successfully!\n")
            return

    print("Student not found.\n")

def main_menu():
    """Displays the main menu and handles user input."""
    while True:
        print("--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
