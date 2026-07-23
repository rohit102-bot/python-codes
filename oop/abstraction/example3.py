import abc
class Shape(abc.ABC):
    def __init__(self):
        self.dim1=None
        self.dim2=None
    def readDim(self):
        self.dim1=float(input(""))
        self.dim2=float(input(""))
    @abc.abstractmethod
    def findArea(self):
        pass

class Triangle(Shape):
    def __init__(self):
        super().__init__()
    def findArea(self):
        return self.dim1*self.dim2*0.5
    
class Rectangle(Shape):
    def __init__(self):
        super().__init__()
    def findArea(self):
        return self.dim1*self.dim2
    

t1=Triangle()
t1.readDim()
print(f"Area:{t1.findArea()}")
r1=Rectangle()
r1.readDim()
print(f"Area:{r1.findArea()}")
