test_tup=(3,7,1,18,9)
k=2
test_tup=sorted(test_tup)
out_tuple=tuple(test_tup[:k])+tuple(test_tup[:-k])
print(out_tuple)