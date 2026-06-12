#without comprehension
list1=[]

for i in range(2):
    row=[]
    for j in range(2):
        values=int(input("enter the values: "))
        row.append(values)
    list1.append(row)

for i in list1:
    for j in i:
        print(j,end=" ")
    print()

#with comprehension
list2=[int(input("enter the values")) for i in range(2) for j in range(2)]
print(list1)
