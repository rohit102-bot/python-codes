import sys
try:
    f=open("file1.txt","r")
    s=f.read()
    print(s)
except:
    e=sys.exc_info()
    print(e)
finally:
    f.close()