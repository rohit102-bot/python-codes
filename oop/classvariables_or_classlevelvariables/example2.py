class Product:
    count=0
    def __init__(self,n,p):
        self.__name=n
        self.__price=p
        Product.count=Product.count+1
    def printProduct(self):
        print(f'{self.__name},{self.__price}')


print(Product.count)
p1=Product("mouse",500)
p2=Product("keyboard",2000)
p1.printProduct()
p2.printProduct()
print(Product.count)