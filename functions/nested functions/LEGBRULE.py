x=100#global scope
def fun1():
    y=200 #local scope of fun1
    def fun2():
        z=100 #local scope of fun2
        print(z)
        print(y)
        print(x)
    fun2()
fun1()