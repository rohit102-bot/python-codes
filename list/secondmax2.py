
list1=list(map(int,input().split()))
print(list1)
fmax=max(list1)
print(fmax)
mc=list1.count(fmax)
print(mc)
print(f"second max is :{list1[fmax-mc]}")