def greet(name, message="Welcome"):
    print(f"{message}, {name}!")

greet("Bob")             # Uses default: "Welcome, Bob!"
greet("Bob", "Goodbye")  # Overrides default: "Goodbye, Bob!"
