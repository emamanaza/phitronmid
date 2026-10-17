class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled

    def __repr__(self):
        return (
            f"Student(student_id={self.student_id!r}, name={self.name!r}, "
            f"department={self.department!r}, is_enrolled={self.is_enrolled!r})"
        )


s1 = Student(1, "Rahim Hasan", "CSE", True)
s2 = Student(2, "Mahim Hasan", "EEE", False)

print(s1)
print(s2)