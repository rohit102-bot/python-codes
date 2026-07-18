class Student:
    __count=0
    @classmethod
    def getstudentcount(cls):
        return cls.__count
    def __init__(self):
        self.__rolno=0
        self.__name=None
        Student.__count=Student.__count+1
    
k=Student.getstudentcount()
print(k)
stud1=Student()
k=Student.getstudentcount()
print(k)
print(Student.getstudentcount())#can be called directly with class name no need to create object