d1={1:"Aman",2:'suman',3:'Aman'}
d2={}
for k,v in d1.items():
    if v not in d2.values():
        d2[k]=v
print(d1)
print(d2)