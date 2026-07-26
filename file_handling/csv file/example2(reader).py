import csv
import sys
try:
    f=open("stud.csv","r",newline="")
    fr=csv.reader(f)
    for row in fr:
        print(row)
 
           
except:
    e=sys.exc_info()
    print(e)
finally:
    f.close()
