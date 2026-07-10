def add(*varg,**kwargs):
    s=0
    for value in varg:
        s=s+value
    for value in kwargs.values():
        s=s+value
    return s

res1=add(10,20,30,40,50)
res2=add(a=10,b=20,c=30)
print(res1)
print(res2)