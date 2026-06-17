a="xyz"
b=" xyz"
print(a==b)
c=b.lstrip()
print(c==a)

print(a)
print(b)
print(c)

s1='****xyz'
print(s1)
s2=s1.lstrip("*")
print(s2)

s3='**$##$$xyz'
s4=s3.lstrip("$#*")
print(s4)