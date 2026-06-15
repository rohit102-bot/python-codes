str1=input("enter the string:")
r=True
for i in str1:
    if i>='A' and i<='Z' or i>='a' and i<='z' or i>='0' and i<='9':
        pass
    else:
        r=False
        break
print(r)