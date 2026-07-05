a={10,20,30,60}
b={40,50,60,10}
c=a.union(b)
print(c)

x={1,2,3}
y={1,2,3,5,6,7}
z={1,2,3,5,6,8,9}
p=x|y|z
print(p)


s1=set("ABC")
print(s1)
s2=set("ABCD")
print(s2)
s3=s1.union(s2)
print(s3)