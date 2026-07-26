import csv
with open("product.csv","r") as f:
    fr=csv.DictReader(f)
    for row in fr:
        print(row)
    for row in fr:
            print(row['pname'],row['price'])