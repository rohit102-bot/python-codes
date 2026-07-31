import re

text = "Python123"

match = re.fullmatch("Python", text)#whole string have to be match

print(match)