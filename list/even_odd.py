list1=[1,2,5,4,3,6,8,9,7,10,33,66]
even=[]
odd=[]
for i in range (len(list1)):
    if list1[i]%2==0:
        even.append(list1[i])
    else:
        odd.append(list1[i])
print(f"even numbers are: {even}")
print(f"odd numbers are: {odd}")