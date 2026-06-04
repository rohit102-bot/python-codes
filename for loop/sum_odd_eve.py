oddsum=0
evensum=0
for i in range (12,38):
    if i%2==0:
        evensum=evensum+i
    else:
        oddsum=oddsum+i

print(f"even sum:{evensum}")
print(f"odd sum:{oddsum}")