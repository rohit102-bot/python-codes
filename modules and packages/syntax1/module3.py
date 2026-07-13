def isEven(num):
    return num%2==0
def isPrime(num):
    c=0
    for i in range(1,num+1):
        if num%i==0:
            c=c+1
    return c==2
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)