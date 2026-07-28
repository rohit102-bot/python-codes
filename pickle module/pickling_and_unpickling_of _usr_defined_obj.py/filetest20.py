#program for pickling
import pickle
import emp
with open("employee.ser","wb") as f:
    emp1=emp.Employee()
    emp2=emp.Employee()
    emp1.setData(101,"naresh",5000)
    emp2.setData(102,"suresh",8000)
    pickle.dump(emp1,f)
    pickle.dump(emp2,f)
print ("employee details are saved within file")