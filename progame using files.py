class Student:
    def __init__(self):
        self.student_list = []
        self.no_of_students = int(input("Enter number of students:"))
        for _ in range(self.no_of_students):
            name = input("Enter student name: ")
            id = int(input("Enter student id: "))
            marks1 = int(input("Enter student marks-1: "))
            marks2 = int(input("Enter student marks-2: "))
            marks3 = int(input("Enter student marks-3: "))
            student_info = {
                'name': name,
                'id': id,
                'marks1': marks1,
                'marks2': marks2,
                'marks3': marks3,
                'avg': (marks1 + marks2 + marks3) / 3,  # Calculate and store average
            }
            student_info['grade'] = self.calculate_grade(student_info['avg'])  # Calculate and store grade
            self.student_list.append(student_info)

    def calculate_grade(self, avg):
        if avg < 35:
            return "Fail"
        elif 35 <= avg < 50:
            return "Third Class"
        elif 50 <= avg < 75:
            return "Second Class"
        else:
            return "First Class"

    def save_to_file(self, filename):
        with open(filename, "a+") as student_info:
            for student in self.student_list:
                student_info.write(f"Name: {student['name']}\n")
                student_info.write(f"ID: {student['id']}\n")
                student_info.write(f"Grade: {student['grade']}\n")
                student_info.write(f"Marks-1: {student['marks1']}\n")
                student_info.write(f"Marks-2: {student['marks2']}\n")
                student_info.write(f"Marks-3: {student['marks3']}\n")
                student_info.write(f"Average: {student['avg']:.2f}\n")  # Format average to 2 decimal places
                student_info.write("\n")
        print("File is created.")

# Usage
if __name__ == "__main__":
    student_records = Student()
    (student_records.save_to_file with open("c:\\suryapythonfile\\tejafiles.txt"))