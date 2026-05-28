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

emp1 = Employee("Rahul", "Sharma", 30000)
emp2 = Employee("Mohnish", "Trivedi", 50000)

print(Employee.count)

# print(Employee.raise_percentage)
# print(emp1.raise_percentage)

# emp1.apply_raise()
# print(emp1.pay)

print(Employee.count)