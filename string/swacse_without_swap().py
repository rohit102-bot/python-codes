str1=input("enter the string:")
str2=""
for i in str1:
    if i>='a' and i<='z':
        str2=str2+chr(ord(i)-32)
    elif i>='A' and i<='Z':
        str2=str2+chr(ord(i)+32)
    else:
        str2=str2+str1

print(str1)
print(str2)

