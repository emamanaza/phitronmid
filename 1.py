class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def __repr__(self):
        return f"Student(name={self.name!r}, roll_number={self.roll_number!r})"


class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


s1 = Student("Rahim", 1)
s2 = Student("Mahim", 2)

StudentDatabase.add_student(s1)
StudentDatabase.add_student(s2)

print(StudentDatabase.student_list)