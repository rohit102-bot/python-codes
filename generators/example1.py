def fun1():
    yield 4
    yield 9
    yield 18

a=fun1()
v1=next(a)
v2=next(a)

print(v1)
print(v2)

for v in a:
    print(v)

b=fun1()
list1=list(b)
print(list1)