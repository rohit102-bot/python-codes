names=["naresh","suresh","ramesh","kishore","rajesh"]
for name in names:
    a=name.startswith('r')
    if a:
        print(name)

for name in names: 
    b=name.startswith(('k','r'))
    if b:
     print(name)

str1="python"