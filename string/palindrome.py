str1=input("enter the string: ")
orig=[]
reversed=[]

for i in str1:
    orig.append(i)

for i in str1[::-1]:
    reversed.append(i)

if orig==reversed:
    print(f"palindrome {reversed}")
else:
    print(f"not palindrome {reversed}")

