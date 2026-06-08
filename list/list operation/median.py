list1=[10,2,6,8,5,6,4,7]
length=len(list1)
median=0
if length%2!=0:
    median=length//2
    print(f"median is :{median}")
else:
    median=len(list1)//2
    print(f"median is : {list1[median]+list1[median-1]//2}")
