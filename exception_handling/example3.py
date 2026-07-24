set1=set()
n=int(input("enter how many elements: "))
for i in range(n):
    values=int(input("enter the values: "))
    set1.add(values)
print(set1)
value=int(input("enter the value to remove: "))
try:
    set1.remove(value)
    print(set1)
except KeyError as k:
    print("given value do not exist ")
    print(k)