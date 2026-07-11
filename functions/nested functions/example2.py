def fun1():
    def fun2():
        print("fun2")
    def fun3():
        print("fun3")
    def fun4():
        print("fun4")
    print("inside fun1")
    fun2()
    fun4()
    fun3()
fun1()