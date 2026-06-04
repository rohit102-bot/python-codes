num=int(input("enter any number: "))       #121
org=num
rev=0
while num>0:
    r=num%10
    rev=(rev*10)+r
    num=num//10
if org==rev:
    print("number is palindrome")

else:
    print("number is not palindrome")