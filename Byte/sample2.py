b1=bytes(10)
print(b1)

b2=bytes(range(65,91))
print(b2)

list1=[65,66,67]
b3=bytes(list1)
print(b3)

b4=bytes(b3)
print(b4)

for values in b3:
    print(values)