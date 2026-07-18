class A:
    x=100#this is class variable
    def __init__(self):
        self.y=200 #this is instance variable

print(A.x)#class variable can be directly used by using class name
objA=A()
print(objA.y)