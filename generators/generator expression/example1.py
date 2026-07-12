even=(value for value in range(1,51) if value%2==0)
for value in even:
    print(value,end=" ")
print()

odd=(i for i in range(1,51) if i%2!=0)
for value in odd:
    print(value,end=" ")
print()

list1=[10,20,30,40,50,60]
reviter=(value for value in list1[::-1])
for i in reviter:
    print(i,end=" ")
print()

