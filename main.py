#Main Program loop 
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
            print("Exiting program... THANK YOU!")
            break
        else:
            print("Invalid choice!")


# Run the program
if __name__ == "__main__":
    main()
