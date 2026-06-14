str1=input("enter the sentence:")
s=str1.split()
rev=" ".join(s[::-1])
revw=str1[::-1]

print(f"reversed string is {rev}")
print(f"reversed with words is {revw}")
