print("****menu****")
print("select one of the option:")
print('''1. for area circle
         2. for area of tringle
         3. for area of rectangle
         4. exit''')

opt=int(input("select the option:"))

match(opt):
    case 1:
        r=float(input("enter the radius:"))
        area=3.14*r*r
        print(f"{area:.2f}")
    case 2:
        b=float(input("enter the base:"))
        h=float(input("enter the height:"))
        area=h*b
        print(f"{area:.2f}")

    case 3:
        l=float(input("enter the length: "))
        b=float(input("enter the breadth:"))
        area=l*b
        print(f"{area:.2f}")
    case 4:
        print("thank you")

    case _:
        print("select valid option")

