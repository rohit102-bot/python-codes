import mysql.connector

con=mysql.connector.connect(database="employee",password="1234",user="root",host="localhost")
print("database connected sucessfully")
print(con)
c=con.cursor()
while True:
    emp_id=int(input("enter the rollno"))
    name=input("enter the name")
    salary=int(input("enter the salary"))
    department=input("enter the department")
    city=input("enter the city")
    try:
        c.execute("insert into employee(emp_id,name,salary,department,city) values(%s,%s,%s,%s,%s)",params=(emp_id,name,salary,department,city))
        print("student details are inserted")
    except:
        print("error inserting student details")
    ans=input("add another student?")
    if ans=="no":
        con.commit()
        break
con.close()