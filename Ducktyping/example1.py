class Book:
    def __init__(self,price,pages):
        self.price=price
        self.pages=pages
    def __len__(self):
        return self.pages

b=Book(200,300)
print(len(b))