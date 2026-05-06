

students = {}


def add_student():
    try:
        sid = input("Enter Student ID: ")
        if sid == "":
            raise ValueError("Student ID cannot be empty.")

        grade = input("Enter Grade: ")
        if grade == "":
            raise ValueError("Grade cannot be empty.")

        grade = float(grade)  
        students[sid] = grade
        print("Student added successfully.")

    except ValueError as e:
        print("Error:", e)


def update_student():
    try:
        sid = input("Enter Student ID to update: ")

        if sid not in students:
            raise KeyError("Invalid Student ID.")

        grade = float(input("Enter new Grade: "))
        students[sid] = grade
        print("Grade updated successfully.")

    except ValueError:
        print("Error: Grade must be a number.")
    except KeyError as e:
        print("Error:", e)


def delete_student():
    try:
        sid = input("Enter Student ID to delete: ")

        if sid not in students:
            raise KeyError("Invalid Student ID.")

        del students[sid]
        print("Student record deleted.")

    except KeyError as e:
        print("Error:", e)


def view_students():
    if not students:
        print("No records found.")
    else:
        print("\nStudent Records")
        for sid, grade in students.items():
            print("ID:", sid, "Grade:", grade)


while True:
    print("\n--- Student Grade Management System ---")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Delete Student")
    print("4. View Students")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            update_student()
        elif choice == 3:
            delete_student()
        elif choice == 4:
            view_students()
        elif choice == 5:
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

    except ValueError:
        print("Error: Please enter a valid number for menu choice.")
