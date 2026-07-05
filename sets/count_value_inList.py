list1=[0,20,30,30,40,50,10,20,60,50]
set1=set(list1)
for value in set1:
    c=list1.count(value)
    print(f'{value}--->{c}')