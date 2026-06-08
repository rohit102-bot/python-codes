list1=[]
n=int(input("enter the number of element: "))
for i in range(n):
    values=int(input("enter the values: "))
    list1.append(values)

print(f"before sorting: {list1}")

for i in range(n):
    for j in range(0,n-1):
        if list1[j]>list1[j+1]:
            tmp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=tmp
print(f"after sorting: {list1}")
