dict1={1: 5, 2: 10, 3: 15, 4: 20, 5: 25}
v=dict1.values()
max1=0
for i in v:
    if i>max1:
        max1=i
min1 = max1  
for i in v:
    if i > 0 and i < min1: 
        min1 = i

print(max1)
print(min1)