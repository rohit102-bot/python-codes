names=["naresh","suresh","ramesh","kishore","rajesh","raman"]
for name in names:
    a=name.endswith('h')
    if a:
        print(name)

for name in names:
    b=name.endswith(('h','e','n'))
    if b:
        print(name)