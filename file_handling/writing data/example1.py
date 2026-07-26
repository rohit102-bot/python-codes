import sys
try:
    f=open("file1.txt","w")
    f.write("python")
    f.write("3.13")
    f.write('''python is 
    a programing language''')
    print("data is written inside the file")

except:
    e=sys.exc_info()
    print(e)
finally:
    f.close()