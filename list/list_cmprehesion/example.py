#list for sqr of 1-21
list1=[num**2 for num in range(1,21)]
print(list1)

#list of 0 filled with 100 values 
list2=[0 for num in range(100)]
print(list2)

#list for alphabet for A-Z
list3=[chr(i) for i in range(65,91) ]
print(list3)

#list for alphabet for a-z
list3=[chr(i) for i in range(97,123) ]
print(list3)

namelist1=["nk","ramesh","suresh","kishore"]
#create copy of list by converting all name is =n upper case
namelist2=[names.upper() for names in namelist1]
print(namelist1)
print(namelist2)

