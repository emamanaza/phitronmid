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
        if not self.is_enrolled:
            self.is_enrolled = True

    def drop_student(self):
        self.is_enrolled = False

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


s1 = Student(1, "Rahim Hasan", "CSE", True)

s1.view_student_info()