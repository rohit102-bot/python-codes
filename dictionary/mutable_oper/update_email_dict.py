email={'rohit':'rohitkalbhor@gmail.com','aman':'aman@gmail.com','suman':'suman@gmail.com'}
name=input("enter the name:")
if name in email:
    print(f"before updating: {email}")
    em=input("enter the new mail:")
    email[name]=em
else:
    print("name not found")

print(f"after updating :{email}")
