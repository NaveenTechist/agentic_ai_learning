#Class Method and Static Method


class Employee:
    raise_percentage = 1.04  # Class Global varible
    count  = 0 # Class Global variable


    __slots__ = ["first", "last", "pay", "email"] # This is enforcing to create only these attributes, sometimes this is stope productions failures
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email =  first.lower() + "." + last.lower() + "@gmail.com"
        Employee.count += 1
        # self.count += 1 # Dont do this sometimes wrong output comes 

    def full_name(self):
        return f"{self.first} {self.last}" 

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_percentage)
        return self.pay

    @classmethod
    def set_raise_percentage(cls, amount):
        cls.raise_percentage = amount

    @classmethod
    def employee_count(cls):
        return cls.count     

    @staticmethod
    def is_workday(day):
        return day.weekday() < 5    # 0 to 5 weekday 6 == Sunday


import datetime



# emp1 = Employee("Rahul", "Sharma", 30000) 
# emp2 = Employee("Mohnish", "Trivedi", 50000)


# emp1.raise_percentage(1.05) 
# print(emp1.raise_percentage)
# print(emp1.employee_count())

# print(Employee.raise_percentage)
# Employee.set_raise_percentage(1.07)
# print(Employee.raise_percentage)

# print(Employee.employee_count())

week_day = datetime.date(2026, 5, 18)
weekend = datetime.date(2026, 5, 24)

# print(Employee.is_workday(week_day))
# print(Employee.is_workday(weekend))


#Example 

class StringHelper:
    @staticmethod
    def snake_case(text):
        return text.lower().replace(" ", "_")

    @staticmethod
    def is_email(mail):
        return "@" in mail and "." in mail 


print(StringHelper.snake_case("Hello World"))
print(StringHelper.is_email("a@.com"))
