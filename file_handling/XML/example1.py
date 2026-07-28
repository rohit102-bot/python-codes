
import xml.etree.ElementTree as ET

tree = ET.parse("student.xml")
root = tree.getroot()

for student in root:
    print(student.find("id").text)
    print(student.find("name").text)
    print(student.find("branch").text)
    print("----------------")