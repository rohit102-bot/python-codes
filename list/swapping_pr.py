list1=[]
n=int(input("enter the number of element: "))
for i in range(n):
    value=int(input("enter the values: "))
    list1.append(value)

print(f"before swapping: {list1}")

pos1=int(input("enter the position1: "))
pos2=int(input("enter the position2: "))
tmp=list1[pos1-1]
list1[pos1-1]=list1[pos2-1]
list1[pos2-1]=tmp
print(f"After swapping the values: {list1}")