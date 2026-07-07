d1={1:10,2:20,3:30,4:40,5:50}
print(d1[1])
print(d1[4])
#print(d1[6])this will raise a ey error

v1=d1.get(1)
print(v1)

v2=d1.get(6)
print(v2)

v4=d1.get(6,60)
print(v4)