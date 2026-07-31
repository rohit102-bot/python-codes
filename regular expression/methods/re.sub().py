import re

text = "I like Python"

result = re.sub("Python", "Java", text)

print(result)

text = "Age: 21, Marks: 95"

result = re.sub(r"\d+", "XX", text)

print(result)