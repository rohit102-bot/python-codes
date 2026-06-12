list1=[]
n=int(input("enter the size of the list: "))
for i in range(n):
    values=int(input("enter the values: "))
    list1.append(values)
#without comprehension 
print(list1)

#with comprehension
list2=[int(input("enter the values of list2:"))for i in range(n)]
print(list2)

