import re

text = "Python Java C++"

result = re.split(r"\s", text)

print(result)



text = "apple,banana;mango orange"

print(re.split(r"[,;\s]+", text))