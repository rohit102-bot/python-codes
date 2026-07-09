def string_con9():
    string=input("enter the string :")
    uc=''
    for ch in string:
        if ch>='a' and ch<='z':
            uc=uc+chr(ord(ch)-32)
        else:
            uc=uc+ch
    return uc

print(string_con9())