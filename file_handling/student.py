
def add_student():
    try:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        if not roll or not name or not marks:
            print("❌ All fields are required.")
            return

        file = open("students.txt", "a")
        file.write(f"\nRoll:{roll},Name:{name},Mark:{marks}")
        file.close()

        print("✅ Student record added successfully.")

    except Exception as e:
        print("Error:", e)


def show_students():
    try:
        file = open("students.txt", "r")
        content = file.read()

        if content == "":
            print("No records found.")
        else:
            print("\n📋 Student Records:")
            print(content)

        file.close()

    except FileNotFoundError:
        print("File not found. No records yet.")


def update_student():
    try:
        roll_to_update = input("Enter Roll Number to update: ")

        file = open("students.txt", "r+")
        data = file.read()

        if data == "":
            print("No records found.")
            file.close()
            return

        records = data.strip().split("\n")
        found = False

        new_data = ""

        for record in records:
            roll, name, marks = record.split(",")

            if roll == roll_to_update:
                new_marks = input("Enter New Marks: ")
                new_data += f"{roll},{name},{new_marks}\n"
                found = True
            else:
                new_data += record + "\n"

        if not found:
            print("❌ Roll Number not found.")
        else:
            file.seek(0)
            file.write(new_data)
            file.truncate()
            print("✅ Marks updated successfully.")

        file.close()

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error:", e)

def main():
    while True:
        print("\n--- Student Record Manager ---")
        print("1. Add New Student")
        print("2. Show All Students")
        print("3. Update Student Marks")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

