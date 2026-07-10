def fun1(a,b,c):
    print(a,b,c)

def fun2(**kwargs):
    print(kwargs['a'],kwargs['b'],kwargs['c'])

fun1(a=10,b=20,c=30)
fun2(a=10,b=20,c=0)