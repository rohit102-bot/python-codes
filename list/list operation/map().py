list1=['10','20','30']
a,b,c=list1
print(a,b,c,type(a),type(b),type(c))

x,y,z=map(int,list1)
print(x,y,z,type(x),type(y),type(z))

p,q,r=map(float,list1)
print(x,y,z,type(p),type(q),type(r))

list2=["java","python","oracle"]
a,b,c=map(str.upper,list2)
print(a,b,c)

list3=list(map(int,list1))
print(type(list3))
print(list3)
