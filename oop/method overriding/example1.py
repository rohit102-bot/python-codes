class Person:
    def __init__(self):
        self.__name=None
    def read(self):
        self.__name=input("enter the name")
    def print_info(self):
        print(f"name:{self.__name}")

class Employee(Person):
    def __init__(self):
        super().__init__()
        self.__job=None

    def read(self):
        super().read()
        self.__job=input("enter job")

    def print_info(self):
        super().print_info()
        print(f"job:{self.__job}")

emp=Employee()
emp.read()
emp.print_info()