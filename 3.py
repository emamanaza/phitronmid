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

    def __repr__(self):
        return (
            f"Student(student_id={self.student_id!r}, name={self.name!r}, "
            f"department={self.department!r}, is_enrolled={self.is_enrolled!r})"
        )


Student(1, "Rahim Hasan", "CSE", True)
Student(2, "Mahim Hasan", "EEE", False)

print(StudentDatabase.student_list)