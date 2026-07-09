a=100

def func1():
    print(a)

def func2():
    global a
    a=500
    print(a)

func1()
func2()
func1()