list1=[1,2,5,4,3,6,8,9,7,10,33,1,23,5,6,-1,6,-8,-7,10]
a=sorted(list1)
max=a[0]
sm=a[0]
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
        sm=a[i-1]    
print(sm)

