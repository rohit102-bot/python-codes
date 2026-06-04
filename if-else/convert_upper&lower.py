ch=input("enter any character")

if ch>='a' and ch<='z':
    ch=chr(ord(ch)-32)
    print(ch)
elif ch>='A' and ch<='z':
    ch=chr(ord(ch)+32)
    print(ch)
else:
    print("input must be a character")