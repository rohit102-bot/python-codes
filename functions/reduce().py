import functools

list1={1,2,3,4,5,6,7,8,9,10}
res1=functools.reduce(lambda x,y:x+y,list1)
print(res1)