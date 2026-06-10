list1=[]
list1.append(10)
print(list1)

#list1.append(20,30) is not allowed ,append takes exacly one argument
list1.extend([20,30])
print(list1)

list1.extend(["NIT"])
print(list1)

list1.extend("NIT")
print(list1)

