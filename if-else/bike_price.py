cost= int(input("enter the cost of the bike:"))

if cost >100000:
    tax_amt=(cost*15)/100

elif cost>50000 and cost<100000:
    tax_amt=(cost*10)/100

else:
    tax_amt=(cost*5)/100

print(f"cost of bike is {cost}")
print(f"tax_amnt is {tax_amt:.2f}")