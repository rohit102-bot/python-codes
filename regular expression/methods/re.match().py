import re

text = "123ABC"

match = re.match(r"\d+", text)

print(match.group())