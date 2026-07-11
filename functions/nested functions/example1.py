def fun():
    print("inside outer function")
    def fun2():
        print("inside inner function")
    fun2()


fun()
