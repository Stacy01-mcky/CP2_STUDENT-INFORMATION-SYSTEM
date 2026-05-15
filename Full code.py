# Full code
# Student Information System

import json
students = []  # Array to store student records
FILE_NAME = "students.json"

# ---------- File Handling ----------
def load_students():
    """Load student records from file if available."""
    global students
    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []

def save_students():
    """Save student records to file."""
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Display menu

def display_menu():

    print("===== Student Information System =====")

    print("1. Add Student")

    print("2. View Students")

    print("3. Search Student")

    print("4. Delete Student")

    print("5. Exit")



# Add student

def add_student():

    name = input("Enter student name: ").strip()

    studentid = input("Enter student ID: ").strip()

    age = input("Enter student age: ").strip()

    birthday = input("Enter student birthday (YYYY-MM-DD): ").strip()

    course = input("Enter student course: ").strip()



    # Input validation

    if not name or not studentid.isdigit() or not age.isdigit() or not course:

        print("Invalid input. Please try again.")

        return



    student = {

        "name": name,

        "studentid": int(studentid),

        "age": int(age),

        "birthday": birthday,

        "course": course

    }

    students.append(student)

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

            print(f"Student {delete_name} deleted successfully!")

            return

    print("Student not found.")



# Main program loop

def main():

    while True:

        display_menu()

        choice = input("Choose your option: ").strip()



        if choice == "1":

            add_student()

        elif choice == "2":

            view_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            delete_student()

        elif choice == "5":

            print("Exiting program... Thanks for using the System!")

            break

        else:

            print("Invalid choice!")



# Run the program

if __name__ == "__main__":

    main()
