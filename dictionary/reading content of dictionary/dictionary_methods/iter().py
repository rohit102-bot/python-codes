dict={1:10,2:20,3:30,4:40}
i=iter(dict)

print(next(i))
print(next(i))
print(next(i))

for keys in dict:
    print(keys,dict[keys])