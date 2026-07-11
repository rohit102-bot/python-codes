def decorator(f):
    def fun1():
        print("$"*100)
        f()
        print("$"*100)
    fun1()

@decorator
def tmp():
    print("hello my name is rohit ")
