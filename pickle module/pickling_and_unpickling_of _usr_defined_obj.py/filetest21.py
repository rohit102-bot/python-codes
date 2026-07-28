#unpickling employee objects
import pickle


with open("employee.ser","rb") as f:
    employee1=pickle.load(f)
    employee2=pickle.load(f)
    print(employee1)
    print(employee2)