from constants import FILE_NAME, students
# ---------- Constants ----------
FILE_NAME = "students.txt"
students = []

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

# ---------- Validation Helpers ----------
def validate_name(name):
    if not re.match(r'^[A-Za-z ]+$', name):
        raise ValueError("Error: Name must contain only letters and spaces.")

def validate_course(course):
    if not re.match(r'^[A-Za-z0-9 ]+$', course):
        raise ValueError("Error: Course contains invalid characters.")

def validate_date(birthday):
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', birthday):
        raise ValueError("Error: Birthday must be in YYYY-MM-DD format.")
    try:
        datetime.strptime(birthday, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Error: Birthday is not a valid calendar date.")
