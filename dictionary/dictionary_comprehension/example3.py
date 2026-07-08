import random
sales1={year:random.randint(10000,60000) for year in range(2001,2011) }
print(sales1)
sales1_dict1={year:sales for year,sales in sales1.items() if sales<50000 }
sales1_dict2={year:sales for year,sales in sales1.items() if sales>50000 }
print(sales1_dict1)
print(sales1_dict2)