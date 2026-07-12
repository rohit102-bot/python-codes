list1=[1,2,3,4,5]
a=map(lambda num:num**2,list1)
for value in a: 
    print(value,end=' ')

print()
list2=["10","20","30","40","50"]
b=map(lambda value:int(value),list2)
list3=list(b)
print(list2)
print(list3)

names=["jnrw","erfv","RFds","dfv"]
n=map(lambda n:n.upper(),names)
list4=list(n)
print(list4)