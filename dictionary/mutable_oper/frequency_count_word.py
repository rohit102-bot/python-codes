str1=input('enter the string:')
list1=str1.split()
d1={}
for value in set(list1):
    c=list1.count(value)
    d1[value]=c

print(d1)