import re

text = """
Rohit: 85
Amit: 92
Rahul: 78
Priya: 95
"""

marks = re.findall(r"\d+", text)

print(marks)