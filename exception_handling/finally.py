try:
    n1=int(input("enter the num1: "))
    n2=int(input("enter the num2: "))
    n3=n1/n2
    print(n3)
except ZeroDivisionError:
    print(" number cannot divide by zero")
except ValueError:
    print("please give valid input")
finally:
    print("inside the finally block")

print("continue........")