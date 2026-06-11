matrix1=[]
matrix2=[]
addmatrix=[]

for i in range(2):
    row=[]
    for j in range(2):
        values=int(input("enter the values of matrix1:"))
        row.append(values)
    matrix1.append(row)

for i in range(2):
    row=[]
    for j in range(2):
        values=int(input("enter the values of matrix2:"))
        row.append(values)
    matrix2.append(row)
print()
print(f"matrix1: {matrix1}")
print()
print(f"matrix2: {matrix2}")

for i in range(2):
    row=[]
    for j in range(2):
        add=matrix1[i][j]+matrix2[i][j]
        row.append(add)
    addmatrix.append(row)

print(f"addition of matrix is :{addmatrix}")


