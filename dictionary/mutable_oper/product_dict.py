product={}
n=int(input("enter the no of product:"))
for i in range(1,n+1):
    pid=int(input(f"enter the '{i}' product id:"))
    pname=input(f"enter the '{i}' product name: ")
    pprice=float(input(f"enter the '{i}' product price: "))
    product[pid]={
        'product_name':pname,
        'product_price':pprice
    }

print(product)