import pickle
with open("file1.ser","wb") as f:
    pickle.dump(65,f)
    pickle.dump(1.5,f)
    pickle.dump(1+2j,f)
    pickle.dump([10,20,30,40,50],f)

    pickle.dump({'empno':[1,2,3],'ename':["naresh",'ramesh','suresh']},f)
print("data is written nside file")