import sys
try:
    f=open("emp.txt","a")
    while True:
        empno=int(input("EmployeeNo: "))
        ename=input("enter the name: ")
        sal=float(input("salary"))
        print(empno,ename,sal,sep=",",file=f)
        ans=input("add another employee?")
        if ans=="no":
            break
except:
    t=sys.exc_info()
    print(t[0])
finally:
    f.close()