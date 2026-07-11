def greet(msg):
    def display(name):
        print(name+""+msg)
    return display

a=greet("hello")
a("rohit")