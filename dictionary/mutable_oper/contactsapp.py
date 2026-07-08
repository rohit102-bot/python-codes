contacts= {"Alice Smith": "+1-555-0198","Bob Jones": "+1-555-0143","Charlie Brown": "+1-555-0177"}
while True:
    print("1.add")
    print("2.update")
    print("3.remove")
    print("4.search")
    print("5.list")
    print("6.exit")
    opt=int(input("enter the option:"))

    if opt==1:
        name=input("name:")
        if name not in contacts:
            mob=int(input("enter the mobile number:"))
            contacts[name]=mob
            print("contact added sucessfully")
        else:
            print(f"{name}exists")
    elif opt==2:
        name=input("enter the name:")
        if name in contacts:
            mob=int(input("enter the mobile no:"))
            contacts[name]=mob
            print("contacts updated sucessfully!")
        else:
            print("contact not found!")
    elif opt==3:
        name=input("enter the name:")
        if name in contacts:
               del(contacts[name])
               print(f"{name} contact deleted sucessfully")
        else:
            print(f"{name} contact not found ")
    elif opt==4:
        name=input("enter the name:")
        if name in contacts:
            print(f"{name} : {contacts[name]}")
        else:
            print(f"{name} contact not found")
    elif opt==5:
        print(contacts)
    elif opt==6:
        break
