students = []

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def add_student():
    name = input("Enter student name: ")
    score = float(input("Enter student score: "))
    grade = calculate_grade(score)

    student = {
        "name": name,
        "score": score,
        "grade": grade
    }

    students.append(student)
    print("Student record added successfully.")

def view_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for s in students:
        print(f"Name: {s['name']}, Score: {s['score']}, Grade: {s['grade']}")

def calculate_average():
    if not students:
        print("No student records found.")
        return

    total = 0
    for s in students:
        total += s["score"]

    average = total / len(students)
    print(f"Average Score: {average:.2f}")

def rank_students():
    if not students:
        print("No student records found.")
        return

    ranked = sorted(students, key=lambda x: x["score"], reverse=True)

    print("\n--- Student Ranking ---")
    rank = 1
    for s in ranked:
        print(f"{rank}. {s['name']} - Score: {s['score']} - Grade: {s['grade']}")
        rank += 1


while True:
    print("\n=== Student Gradebook System ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Calculate Average Score")
    print("4. Rank Students")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        calculate_average()

    elif choice == "4":
        rank_students()

    elif choice == "5":
        print("Exiting Student Gradebook System.")
        break

    else:
        print("Invalid choice. Please try again.")

