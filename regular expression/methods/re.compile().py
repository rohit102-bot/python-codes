import re

text="compile fuction is used to compile regular expresssion into a pattern object"
pattern=re.compile(r'\b\w{4}\b')#compiled pattern once and can be used again
for match in pattern.findall(text):
    print(match)

p=r'\b\w{4}\b'
for match in re.findall(p,text):#compiled each time it runs
    print(match)

#difference is just about time complexity