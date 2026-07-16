class Student:
    def __init__(self,r,n,c):
        self.__roll_no=r
        self.__name=n
        self.__course=c
    def stud_details(self):
        print(f"student name is {self.__name},student roll no is {self.__roll_no},course is {self.__course}")

stud1=Student(82,'rk','comp')
stud1.stud_details()

