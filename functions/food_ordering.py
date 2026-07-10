def place_order(customer_name,**items):
    if not  items:
        print(f"Hello {customer_name}, you havent ordered anything yet")
        print(f"you can choose from this menu: {menu}")
        return
    print(f"\n order summery for {customer_name}:")

    total_price=0

    menu={
        "burger":120,
        "pizza":250,
        "pasta":180,
        "coffee":80,
        "fries":100
    }

    for item,quantity in items.items():
        if item in menu:
            price=menu[item]*quantity
            total_price+=price
            print(f"{item.capitalize()}*{quantity}")
        else:
            print(f"sorry {item} is not available")
        

    print(f"total bill is {total_price} ")

place_order("rohit",burger=2,pizza=1)