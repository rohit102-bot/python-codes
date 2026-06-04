string=input("enter the string: ")
ac=0
dc=0
sc=0

for ch in string:
    if ch>='a' and ch>='A':
        ac+=1
    elif ch>='0' and ch<='9':
        dc+=1
    else:
        sc+=1
print(f"alphabets in string are:{ac}")
print(f"digit count in string are:{dc}")
print(f"special character in string are:{sc}")