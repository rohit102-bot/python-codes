import json
with open("emp.json","w") as f:
    emp_dict={'empno':[1,2,3],
            'ename':['nk','suresh','kishore'],
            'salary':[4500,5000,6000]}
    json.dump(emp_dict,f)