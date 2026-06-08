list1=["rohit","ram","sham","rahul","jay"]
a=iter(list1)
n1=a.__next__()#gives the first value to n1
print(n1)
for n in a:
    print(n)#now all values ater first value will be printed