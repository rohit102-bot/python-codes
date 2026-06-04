salary=int(input("enter your salary:"))
years= int(input("years of service "))

if years>10:
    bonus=(salary*10)/100

elif years >=6 and years<=10:
    bonus=(salary*8)/100
else:
    bonus=(salary*5)/100

print(f"your net bonus amount is {bonus}")