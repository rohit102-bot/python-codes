m=int(input("enter the 1st number: "))
n=int(input("enter the 2nd number: "))
even=[]

for i in range(m,n):
    if i%2==0:
      even.append(i)

print(f"even numbers between m and n are:{even}")