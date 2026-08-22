import mysql.connector

cn=mysql.connector.connect(database='employee',user='root',password='1234',host='localhost')

print("connection is established successfully..")
print(cn)