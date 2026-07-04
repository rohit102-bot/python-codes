ba1=bytearray()
print(ba1)

bytearray(b'')
ba1.append(65)
print(ba1)

ba1.append(66)
print(ba1)

ba1.extend([67,68,69,70])
print(ba1)

ba1[0]=71
print(ba1)

del ba1[0]
print(ba1)

ba2=bytearray(10)
print(ba2)

ba2[0]=65
print(ba2)

ba2[-1]=90
print(ba2)

ba3=bytearray(range(97,123))
print(ba3)

