str1="a,b,c,d,e"
t=str1.partition(",")
print(type(t))
print(t)

str2="xyzw"
t2=str2.partition("y")
print(t2)

str3="xyz:abc:pqr"
t3=str3.partition(":")
print(t3)

name="rama rao"
t4=name.partition(" ")
print(t4)
print(f"firstname:{t4[0]}")
print(f"last name:{t4[-1]}")