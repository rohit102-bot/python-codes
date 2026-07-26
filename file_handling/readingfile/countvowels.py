import sys
try:
    f=open("file1.txt","r")
    c=0
    while True:
        s=f.read(1)
        if s=="":
            break
        if s in "aeiouAEIOU":
            c+=1
    print(f"COUNT of vowels is {c}")

except:
    e=sys.exc_info()
    print(e)
finally:
    f.close()    
