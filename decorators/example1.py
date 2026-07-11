def drawstar(fun1):
    def draw():
        print("*"*40)
        fun1()
        print("*"*40)
    return draw

@drawstar
def display():
    print("PYTHON")
@drawstar
def studinfo():
    print("rollno:101")
    print("name: rajesh")

display()
studinfo()