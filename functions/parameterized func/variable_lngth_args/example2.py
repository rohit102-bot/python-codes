def add(*values):
    s=0
    for values in values:
        s=s+values
    return s

res1=add(10,20)
res2=add(10,20,30,40,50)
print(f"sum of two numbers {res1}")
print(f"sum of two numbers {res2}")