def reviter(s):
    s=s[::-1]
    for x in s:
        yield x

list1=[10,20,30,40,50,60]
a=iter(list1)
for x in a:
    print(x,end="") 
    print()
    
print("**************************")

b=reviter(list1)
for y in b:
    print(y,end='')
    print()