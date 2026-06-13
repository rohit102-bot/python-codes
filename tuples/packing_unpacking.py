#packing
t1=10,20,30
print(t1)
print(type(t1))

#unpacking
a,b,c=10,20,30
print(a,b,c)
print(type(a),type(b),type(c))

#a,b,c=(10,20,30,40,50,60)#this throw value error,too many values to unpack

a,b,c,*d=(10,20,30,40,50,60)#first 3 elements in a,b,c and rest will be in d
print(a,b,c,d)