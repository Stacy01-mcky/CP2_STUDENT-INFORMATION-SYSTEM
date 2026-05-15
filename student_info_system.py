# Student Information System
# Requirements: Functions, Arrays, Looping Menu, Input Validation, Clean Code
# OLIVEROS(INTRO - VIEW STUDENT) 
# INSORIO ( SEARCH - END)
# MY INTRO CODE
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
    print("=== Student Information System ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit!! ")

