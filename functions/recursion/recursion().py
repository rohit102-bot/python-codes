import sys

def hello():
    print("hello")
    hello()
s=sys.getrecursionlimit()
print(s)
sys.setrecursionlimit(50)
hello()