def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    totalmarks = input("enter the total  marks : ")
    classs = input("enter the  classs : ")

    with open("d:\\suryapythonfiles\\tejafile.txt", "a+") as file:
        file.write(f"| {student_id}| , |{name}| , |{grade}| , |{totalmarks}| , |{classs}|\n")
    print("Student record added successfully.")


while True:
    print("\nStudent Data Management System")
    print("1. Add Student")
    print("2. Exit")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        break
    else:
        print("Invalid choice. Please enter 1, 2")

