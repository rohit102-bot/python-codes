from operator import itemgetter
list1=[{'name':'nandini','age':20},{'name':'manjeet','age':20},{'name':'nikhil','age':19}]
lis2=sorted(list1,key=itemgetter('age'))
print(lis2)