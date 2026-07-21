import abc
class A(abc.ABC):
    @abc.abstractmethod
    def m1(self):
        pass
class B(A):
    def m1(self):
        print("over riding")
    
objb=B()
objb.m1()