students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        students.append({"name": name, "roll": roll})
        print("Student added successfully!")

    elif choice == "2":
        for student in students:
            print(student)

    elif choice == "3":
        roll = input("Enter roll number to search: ")
        found = False
        for student in students:
            if student["roll"] == roll:
                print(student)
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter roll number to delete: ")
        students = [s for s in students if s["roll"] != roll]
        print("Student deleted.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")
