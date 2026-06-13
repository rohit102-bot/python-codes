
s1=input("input numbers seperated by space: ")
list1=s1.split()
print(list1)

list2=[int(i) for i in list1 ]
s=0
for i in list2:
    s=s+i

print(s)


