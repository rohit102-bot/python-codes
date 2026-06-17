s1='testhook'
s2=s1.removeprefix('test')
print(s2)
s3=s1.removeprefix('hook')#hook will not be removed bcs this function only works on starting values
print(s3)

s4=s1.lstrip('test')
print(s4)