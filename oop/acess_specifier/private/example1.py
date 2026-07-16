class A:
    def __init__(self):
        self.x=10
        self.__y=20
    def __m1(self):
        print("private method")
    def m2(self):
        print("this is public method")
        print(f"y={self.__y}")
        self.__m1()

obja=A()
print(obja.x)
#print(obja.__y) it cannot b acessed it is a private member
obja.m2()#public method of same class can acess 
#obja,__m1() cannot call the private method
