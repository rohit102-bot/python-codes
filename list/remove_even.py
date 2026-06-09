list1=[4,9,2,3,5,1,11,13,17,23,8,12,16,18,20,22]
i=0
while i<len(list1):
    if list1[i]%2==0:
        del list1[i]
    else:
        i+=1 # if condotion of deletion is satisfied then delete else skip 

print(list1)

