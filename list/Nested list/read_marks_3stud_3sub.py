stud=[]
for i in range(3):
    mrow=[]
    for j in range(3):
        marks=int(input((f"enter the marks if student{i+1}: ")))
        mrow.append(marks)
    stud.append(mrow)
print(stud)