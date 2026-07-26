import sys
try:
    f=open("emp.txt","r")
    total=0
    while True:
        s=f.readline()
        if s =='':
            break
        list1=s.split(",")
        sal=float(list1[2])
        total=total+sal
        print(s,end="")
        print("total salary is : ",total)
except:
    e=sys.exc_info()
    print(e)
finally:
    f.close()