list1=[10,20,30,40,50,60]

del list1[0]
print(list1)

del list1[-2]
print(list1)

del list1[3]
print(list1)

list2=[10,20,30,40,50,60]

del list2[0:7]
print(list2)

list3=list(range(10,110,10))
print(list3)

del list3[0:3]
print(list3)

del list3[-3]
print(list3)

del list3[1:-1]
print(list3)

list4=list(range(10,110,10))
print(list4)

del list4[::2]
print(list4)

list5=list(range(10,110,10))
print(list5)

del list5[::-2]
print(list5)