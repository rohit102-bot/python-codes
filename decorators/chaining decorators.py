def drawstar(f):
    print("*"*100)
    f()
    print("*"*100)

def drawdollar(f):
    print("$"*100)
    

@drawdollar
@drawstar
def display():
    print("myname is rohit")
