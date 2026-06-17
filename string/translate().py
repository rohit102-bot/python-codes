table1=str.maketrans("aeiou","!@#$%")
str1="programming"
str2=str1.translate(table1)
print(str2)

table2=str.maketrans("!@#$%","aeiou")
str4="!@!!JHB@JH#!"
str3=str4.translate(table2)
print(str3)

table5=str.maketrans("aeiou","!@#$%","1234567890")
str6="pyhton312"
str7=str6.translate(table5)
print(str7)