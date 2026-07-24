set1=set()
n=int(input("enter the how many elemennts: "))
for i in range(n):
    vaules=int(input("enter the values: "))
    set1.add(vaules)

v=int(input("enter the value to remove: "))

try:
    set1.remove(v)
except KeyError:
    print("value not present")

print(set1)
