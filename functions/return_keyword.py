#return one value
def add(a, b):
    return a + b  # Sends the sum back

result = add(5, 10)
print(result)  # Output: 15

#returnin multiple values
def get_user():
    name = "Alice"
    age = 25
    return name, age  # Returns ("Alice", 25)

user_name, user_age = get_user()  # Unpacking the tuple
print(user_name)  # Output: Alice
