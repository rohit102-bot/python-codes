list1=[1,2,3,45,34,45,76,33,98,56,12,43,65,93,42,19,73]
list12=[]
even=[]
odd=[]
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(f"even numbers in list are: {even}")
print(f"odd number in list are: {odd}")