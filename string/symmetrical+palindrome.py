str1=input("enter the string: ")
rev=str1[::-1]
l=len(str1)
m=l//2
if l % 2 == 0:
    str3 = str1[:m]
    str4 = str1[m:]
else:
    str3 = str1[:m]
    str4 = str1[m+1:]

if str3==str4 and str1==rev:
    print("string is symmetrical and palindrome")

elif str3==str4:
    print("string is symmetrical")

elif str1==rev:
    print("strin is palindrome")

else:
    print("string is a normal string ") 
