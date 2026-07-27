import json
with open ("emp.json","r") as f:
    d1=json.load(f)
    for k,v in d1.items():
        print(k,v)



with open ("emp.json","r") as f:
    d1=json.load(f)
    print(d1)