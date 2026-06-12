# ---------- Constants ----------
FILE_NAME = "students.txt"
students = []
# Display menu
def display_menu():
    print("----------Student Information System--------------------")
    print("--------------------------------------------------------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit!!")
    print("--------------------------------------------------------")

import re
from datetime import datetime

# Add student
def add_student():
    name = input("Enter student name : ").strip()
    studentid = input("Enter student ID : ").strip()
    age = input("Enter student age : ").strip()
    birthday = input("Enter student birthday (YYYY-MM-DD): ").strip()
    course = input("Enter student course: ").strip()

    # Regex for name (letters and spaces only)
    valid_name_pattern = re.compile(r'^[A-Za-z ]+$')
    # Regex for course (letters, numbers, and spaces allowed)
    valid_course_pattern = re.compile(r'^[A-Za-z0-9 ]+$')

    # Validate student ID (only digits)
    if not studentid.isdigit():
        raise ValueError("Error: Student ID must contain only numbers.")

    # Validate age (only digits)
    if not age.isdigit():
        raise ValueError("Error: Age must contain only numbers.")

    # Validate name (only letters and spaces)
    if not valid_name_pattern.match(name):
        raise ValueError("Error: Name must contain only letters and spaces.")

    # Validate course (letters, numbers, spaces)
    if not valid_course_pattern.match(course):
        raise ValueError("Error: Course contains invalid characters (only letters, numbers, and spaces allowed).")

    # Validate birthday: only numbers and dashes allowed
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', birthday):
        raise ValueError("Error: Birthday must contain only numbers and dashes in YYYY-MM-DD format.")

    # Check if it's a real date (rejects impossible dates like 2026-02-30)
    try:
        datetime.strptime(birthday, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Error: Birthday is not a valid calendar date.")

    student = {
        "name": name,
        "studentid": int(studentid),
        "age": int(age),
        "birthday": birthday,
        "course": course
    }
    students.append(student)
    save_students()
    print(f"Student {name} added successfully!")



# View all students
def view_students():
    if not students:
        print("No student records found.")
        return
    print("--- Student Records ---")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, ID: {student['studentid']}, Age: {student['age']}, Birthday: {student['birthday']}, Course: {student['course']}")


# Search student by name
def search_student():
    search_name = input("Enter student name to search: ").strip()
    found = False
    for student in students:
        if student["name"].lower() == search_name.lower():
            print(f"Found: Name: {student['name']}, ID: {student['studentid']}, Age: {student['age']}, Birthday: {student['birthday']}, Course: {student['course']}")
            found = True
            break
    if not found:
        print("Student not found.")


# Delete student by name
def delete_student():
    delete_name = input("Enter student name to delete: ").strip()
    for student in students:
        if student["name"].lower() == delete_name.lower():
            students.remove(student)
            save_students()
            print(f"Student {delete_name} deleted successfully!")
            return
    print("Student not found.")
