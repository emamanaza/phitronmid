class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.is_enrolled:
            print(f"Error: {self.name} is already enrolled.")
        else:
            self.is_enrolled = True
            print(f"{self.name} has been enrolled.")

    def drop_student(self):
        if not self.is_enrolled:
            print(f"Error: {self.name} is not enrolled.")
        else:
            self.is_enrolled = False
            print(f"{self.name} has been dropped.")

    def view_student_info(self):
        print(self.student_id, self.name, self.department, self.is_enrolled)


Student(1, "Rahim Hasan", "CSE", True)
Student(2, "Mahim Hasan", "EEE", False)


def find_student(sid):
    for s in StudentDatabase.student_list:
        if s.student_id == sid:
            return s
    return None


while True:
    print("\n1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for s in StudentDatabase.student_list:
            s.view_student_info()
    elif choice == "2" or choice == "3":
        try:
            sid = int(input("Enter student ID: "))
        except ValueError:
            print("Error: Student ID must be a number.")
            continue

        student = find_student(sid)
        if student is None:
            print("Error: Invalid student ID.")
        elif choice == "2":
            student.enroll_student()
        else:
            student.drop_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice")