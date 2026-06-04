num=int(input("enter the number"))

last_digit=num%10

if last_digit%2==0:
    print(f"last number {last_digit} is even")
else:
    print(f"last digit {last_digit} is odd")
