unit=int(input("enter the unit of eklectricity"))
if unit==100:
    amt=0
    print(f"no charge so {amt} rs")
elif unit>100 and unit<200:
    amt=(unit-100)*5
    print(f"rs 5 per unit so {amt} rs")

elif unit>200:
    amt=0+500+(unit-200)*10
    print(f"rs 10 per unit so {amt} rs")
