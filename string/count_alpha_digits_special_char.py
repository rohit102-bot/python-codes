str1=input(("enter the string: "))
cr=0
sc=0
num=0
for i in str1:
    if i>='A' and i<='Z' or i>='a' and i<='z':
        cr+=1
    elif i>='0' and i<='9':
        num+=1
    else:
        sc+=1
print(cr,sc,num)
