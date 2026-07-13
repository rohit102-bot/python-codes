import sys

def rev(num):
        if num<5:
            num=num+1
            print(num)
            rev(num)


rev(0)
