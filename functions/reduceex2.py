import functools
def add(x,y):
    return x+y
def maxi(a,b):
    if a>b:
        return a
    else:
        return b

list1=[12,34,5,51,76]
a=functools.reduce(add,list1)
b=functools.reduce(maxi,list1)
print(a)
print(b)
