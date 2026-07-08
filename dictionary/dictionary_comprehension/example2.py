grade_dict={'nk':'A','suresh':'B','ramesh':'A','kishore':'B'}
print(grade_dict)

gradeA_dict={name:grade for name,grade in grade_dict.items() if grade=='A' }
print(gradeA_dict)

grade_dictB={name:grade for name,grade in grade_dict.items() if grade=='B'}
print(grade_dictB)