import csv
import sys

try:
    f=open("stud.csv","w",newline="")
    fw=csv.writer(f)
    while True:
        rollno=int(input("Rollno:"))
        name=input("Name:")
        course=input("course:")
        fw.writerow([rollno,name,course])
        ans=input("Add another student?")
        if ans=='no':
            break
except:
    t=sys.exc_info()
    print(t)
finally:
    f.close()