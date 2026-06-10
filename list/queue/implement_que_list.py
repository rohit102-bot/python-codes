q=[]
while True:
    print("""1.adding
2.removing
3.display
4.exit""")
    option=int(input("select the option: "))
    match(option):
        case 1:
            length=int(input("enter the length of list: "))
            for i in range(length):
                values=int(input("enter the values :"))
                q.append(values)
                print("elements added sucessfully !")
        case 2:
            del q[0]
            print("one element deleted!")
        case 3:
            print(f"elements in queue are :")
            for i in q:
                print(i)
        case 4:
            break
        case _:
            print("invalid option")