def fun1():
    a=100
    def fun2():
        print(a)
    def fun3():
        nonlocal a
        a=500
        print(a)
    fun2()
    fun3()
    print(a)
fun1()