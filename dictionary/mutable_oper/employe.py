emp_dict={1:('narsh',5000),2:('suresh',6000),3:('ramesh',7000)}
print(emp_dict)
id=int(input("enter the emp no to update:"))
if id in emp_dict:
    d=list(emp_dict[id])
    if d[1]<25000:
        d[1]=d[1]+1000
        emp_dict[id]=tuple(d)
print(emp_dict)
