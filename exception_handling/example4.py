try:
    n1=int(input("enter num1: "))
    n2=int(input("enter num2: "))

    n3=n1/n2
except ZeroDivisionError:
    print("number cannot divide by zero: ")
except ValueError:
    print("please enter a valid value ")