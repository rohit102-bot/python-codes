class Employee:
    company = "OpenAI"

    @classmethod
    def change_company(cls, name):
        cls.company = name

    @staticmethod
    def calculate_bonus(salary):
        return salary * 0.10

Employee.change_company("Google")

print(Employee.company)
print(Employee.calculate_bonus(50000))