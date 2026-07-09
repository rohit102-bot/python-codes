x=100
def fun1():
    x=200
    y=300
    print(x)
    print(y)
    a=globals()
    print(a['x'])
    a['x']=900

fun1()
print(x)