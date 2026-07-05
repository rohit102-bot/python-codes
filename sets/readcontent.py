a={10,20,30,40,50}

#using for loop
for value in  a:
    print(value)
print("******************************************")

#using iterator
x=iter(a)
value1=next(x)

print(value1)
value2=next(x)
print(value2)

#using enumerator
t1=enumerate(a)
t2=enumerate(a)
y=next(t1)
print(y)
z=next(t1)
print(z)