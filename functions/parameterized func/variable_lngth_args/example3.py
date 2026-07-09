def maximum(*values):
    m=0
    for i in range(len(values)):
        if i==0:
            m=values[i]
        elif values[i]>m:
            m=values[i]
    return m


m1=maximum(10,20)
m2=maximum(40,20,10)
print(f"maximum of two values {m1}")
print(f"maximum of three values {m2}")