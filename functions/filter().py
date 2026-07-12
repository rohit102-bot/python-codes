list1=[1,3,6,8,9,24,56,89,12,11]
a=filter(lambda value:value%2==0,list1)

for value in a:
    print(value)
print()