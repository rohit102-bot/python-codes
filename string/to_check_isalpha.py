str1=input("enter a string:")
r=True

for i in str1:
    if i>='A' and i<='Z' or i>='a' and i<='z':
        r=True
        pass
    else:
        r=False
        break
print(r)