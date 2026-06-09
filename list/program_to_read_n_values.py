list1=[]
n=int(input("how many values do you want to enter: "))
for i in  range(0,n):
    values=int(input("enter the values: "))
    list1.append(values)

print(f"Before deleting the values: {list1}")

delete=int(input(f"Enter the value you want to delete:"))
if delete in list1:
    i=list1.index(delete)
    del list1[i]

else:
    print(f"Element {delete} not present in list ")

print(f"list after deleting the element : {list1}")

