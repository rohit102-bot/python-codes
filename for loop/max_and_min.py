
first_num = int(input("Enter number 1: "))
greatest = first_num
smallest = first_num

for i in range(2):
    num = int(input(f"Enter number {i+2}: "))
    if num > greatest:
        greatest = num
    if num < smallest:
        smallest = num

print(f"Greatest: {greatest}")
print(f"Smallest: {smallest}")
