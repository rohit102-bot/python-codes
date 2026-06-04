import random
username=str(input("enter your username:"))
otp=random.randint(1000,9000)
print(f"your otp is {otp}")
otp2=int(input("enter your otp:"))
if otp2==otp:
    print("welcome")
else:
    print("invalid otp")