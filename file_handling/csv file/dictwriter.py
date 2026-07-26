import csv
with open("product.csv","w",newline='') as f:
    fw=csv.DictWriter(f,fieldnames=['pname','price'])
    fw.writeheader()
    while True:
        pn=input("product name: ")
        p=int(input("price: "))
        d={'pname':pn,'price':p}
        fw.writerow(d)
        ans=input("add another product?")
        if ans=='no':
            break