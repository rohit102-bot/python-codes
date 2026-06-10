list1=[[10,20],30]
print(list1)

list2=list1.copy()
print(list2)

list1[0].append(40)
print(list1)
print(list2)

list2[0][0]=99
print(list2)
print(list1)

list1[1]=88
print(list1)
print(list2)#no change in outer list when shallow copy is created,for that purpose you need to create deep copy 

