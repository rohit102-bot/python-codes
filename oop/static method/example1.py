class Student:
    a=10
    b=20
    @staticmethod
    def add():
        return Student.a + Student.b

print(Student.add())