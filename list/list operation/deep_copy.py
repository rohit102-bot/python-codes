list1=[[10,20],30]
print(list1)

import copy #inbuild module for deep copy
list2=copy.deepcopy(list1)

list1[1]=88
print(list1)
print(list2)

list1[0][0]=99
print(list1)
print(list2)

#now both lists are completetly indepenent and does not effect each other 