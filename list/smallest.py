list1=[1,2,5,4,3,6,8,9,7,10,33,1,23,5,6,-1,6,-8,-7,10]
smallest=list1[0]
for i in list1:
    if i<smallest:
      smallest=i
print(smallest)