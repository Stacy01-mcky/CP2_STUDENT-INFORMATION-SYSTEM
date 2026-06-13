import re from datetime
import datetime
#--------Core operations---------
def add_student():
    name = input("Enter student name : ").strip()
    studentid = input("Enter student ID : ").strip()
    age = input("Enter student age : ").strip()
    birthday = input("Enter student birthday (YYYY-MM-DD): ").strip()
    course = input("Enter student course: ").strip()

    if not studentid.isdigit():
        raise ValueError("Error: Student ID must contain only numbers.")
    if not age.isdigit():
        raise ValueError("Error: Age must contain only numbers.")

    validate_name(name)
    validate_course(course)
    validate_date(birthday)

    student = {
        "name": name,
        "studentid": int(studentid),
        "age": int(age),
        "birthday": birthday,
        "course": course
    }
    students.append(student)
    save_students()
    print(f" Student {name} added successfully!")

def view_students():
    if not students:
        print("No student records found.")
        return
    print("--- Student Records ---")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, ID: {student['studentid']}, Age: {student['age']}, Birthday: {student['birthday']}, Course: {student['course']}")

def search_student():
    search_term = input("Search by (1) Name or (2) ID: ").strip()
    if search_term == "1":
        search_name = input("Enter student name: ").strip()
        results = [s for s in students if s["name"].lower() == search_name.lower()]
    elif search_term == "2":
        search_id = input("Enter student ID: ").strip()
        results = [s for s in students if str(s["studentid"]) == search_id]
    else:
        print("Invalid choice.")
        return

    if results:
        for s in results:
            print(f"Found: {s}")
    else:
        print("Student not found.")

def delete_student():
    delete_id = input("Enter student ID to delete: ").strip()
    if not delete_id.isdigit():
        print("Invalid ID.")
        return
    for student in students:
        if student["studentid"] == int(delete_id):
            confirm = input(f"Are you sure you want to delete {student['name']}? (y/n): ").strip().lower()
            if confirm == "y":
                students.remove(student)
                save_students()
                print(f" Student {student['name']} deleted successfully!")
            return
    print("Student not found.")

def update_student():
    update_id = input("Enter student ID to update: ").strip()
    if not update_id.isdigit():
        print("Invalid ID.")
        return
    for student in students:
        if student["studentid"] == int(update_id):
            print(f"Updating record for {student['name']}")
            new_name = input("Enter new name (leave blank to keep current): ").strip()
            new_age = input("Enter new age (leave blank to keep current): ").strip()
            new_course = input("Enter new course (leave blank to keep current): ").strip()

            if new_name:
                validate_name(new_name)
                student["name"] = new_name
            if new_age.isdigit():
                student["age"] = int(new_age)
            if new_course:
                validate_course(new_course)
                student["course"] = new_course

            save_students()
            print(" Student record updated successfully!")
            return
    print("Student not found.")

def show_statistics():
    if not students:
        print("No records to analyze.")
        return
    avg_age = sum(s["age"] for s in students) / len(students)
    print(f" Total Students: {len(students)}")
    print(f"Average Age: {avg_age:.2f}")
    courses = {}
    for s in students:
        courses[s["course"]] = courses.get(s["course"], 0) + 1
    print("Students per Course:")
    for course, count in courses.items():
        print(f"   {course}: {count}")

# ---------- Menu ----------
def display_menu():
    print("\n---------- Student Information System ----------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Show Statistics")
    print("7. Exit")
    print("------------------------------------------------")
