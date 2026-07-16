class A:
    def __init__(self):
        self._protected_var = "Hello from Class A"  # Protected (single underscore)

class B(A):
    def display(self):
        # Subclasses can freely use protected variables from the parent class
        print(self._protected_var)

# --- Using the classes ---

obj = B()
obj.display()  # Output: Hello from Class A

# Python does NOT block this, but you should avoid doing it:
print(obj._protected_var)  
