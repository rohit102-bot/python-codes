class Triangle:
    def __init__(self):
        self.base=0.0
        self.height=0.0

    def setbase(self,b):
        self.base=b
    def setheight(self,h):
        self.height=h
    def findArea(self):
        return self.base*self.height*0.5
    
t1=Triangle()
t1.setbase(1.5)
t1.setheight(1.7)
area=t1.findArea()
print(f'Area of triangle is {area:2f}')

