#any() returns true if any element is true 
list1=[]
print(any(list1))

list2=[0,0,0]
print(any(list2))

list3=[1,2,3,4]
print(any(list3))

list4=[-1,6,8,0]
print(any(list4))

list5=["java","python"]
print(any(list5))

print("all():")#all() returns true only if all elements is true or if iterable is empty 
print(all(list1))
print(all(list2))
print(all(list3))
print(all(list4))

