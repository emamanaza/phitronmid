class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

    @classmethod
    def find_student(cls, student_id):
        for student in cls.student_list:
            if student.student_id == student_id:
                return student
        return None


class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if not self.is_enrolled:
            self.is_enrolled = True
            print(f"{self.name} has been enrolled.")
        else:
            print(f"{self.name} is already enrolled.")

    def drop_student(self):
        self.is_enrolled = False
        print(f"{self.name} has been dropped.")

    def view_student_info(self):
        status = "Enrolled" if self.is_enrolled else "Not Enrolled"
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Enrollment Status: {status}")

    def __repr__(self):
        return (
            f"Student(student_id={self.student_id!r}, name={self.name!r}, "
            f"department={self.department!r}, is_enrolled={self.is_enrolled!r})"
        )


Student(1, "Rahim Hasan", "CSE", True)
Student(2, "Mahim Hasan", "EEE", False)


def get_student_by_input():
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return None
    student = StudentDatabase.find_student(student_id)
    if student is None:
        print("Student not found.")
    return student


def main():
    while True:
        print("\n===== Student Menu =====")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            if not StudentDatabase.student_list:
                print("No students found.")
            for student in StudentDatabase.student_list:
                print()
                student.view_student_info()
        elif choice == "2":
            student = get_student_by_input()
            if student:
                student.enroll_student()
        elif choice == "3":
            student = get_student_by_input()
            if student:
                student.drop_student()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


main()