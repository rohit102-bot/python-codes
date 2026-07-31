import re
text="abc123xyz"
match=re.search(r"\d+",text)
print(match)