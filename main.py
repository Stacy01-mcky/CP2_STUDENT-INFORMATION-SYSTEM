# ---------- Main Loop ----------
from file_handler import load_students
from operations import add_student, view_students, search_student, delete_student, update_student, show_statistics
def main():
    load_students()
    while True:
        display_menu()
        choice = input("ENTER A CHOICE : ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            show_statistics()
        elif choice == "7":
            print("Exiting program... THANK YOU!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
