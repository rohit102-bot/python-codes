class Employee:
    def __init__(self):
        self.__empno=None
        self.__ename=None
        self.__salary=None
    def setData(self,eno,en,s):
        self.__empno=eno
        self.__ename=en
        self.__salary=s
    def __str__(self):
        return f'{self.__empno},{self.__ename},{self.__salary}'