class A:
    x = 100

    class B:
        def m2(self):
            print(A.x)

b = A.B()
b.m2()