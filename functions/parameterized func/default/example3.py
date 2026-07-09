def fun1(a):
    a[0]=99
    a.append(100)
    
def fun2():
    list1=[10,20,30]
    print(f"before calling funtion{list1}")

    fun1(list1)
    print(f"after calling funtion{list1}")

fun2()