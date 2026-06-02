FILE_NAME = "students.txt"

# ---------- File Handling ----------
def load_students():
    """Load student records from file if available."""
    global students
    students = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 5:
                    name, studentid, age, birthday, course = data
                    students.append({
                        "name": name,
                        "studentid": int(studentid),
                        "age": int(age),
                        "birthday": birthday,
                        "course": course
                    })
    except FileNotFoundError:
        print("No records found yet.")

def save_students():
    """Save student records to file."""
    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(f"{student['name']},{student['studentid']},{student['age']},{student['birthday']},{student['course']}\n")
