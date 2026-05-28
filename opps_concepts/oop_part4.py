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


class Developer(Employee):
    pass 
    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay) # Calling parent class constructor
        self.pro_lang = pro_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay) # Calling parent class constructor
        if employees is None:
            self.employees = []
        else:
            self.employees = employees        
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print(f"-> {emp.full_name()}")

    def apply_raise(self):
        super().apply_raise()
        for emp in self.employees:
            emp.apply_raise( )        
        

dev1 = Developer("John", "Doe", 50000, "Python")  
dev2 = Developer("Steve", "Jobs", 60000, "Python")

man = Manager("Jane", "Doe", 60000, [dev1])

man.print_emp()

man.add_emp(dev2)
man.print_emp()

man.remove_emp(dev1)  
man.print_emp()







# print(dev1.email) # Accessing parent class method
# print(dev1.pro_lang) # Accessing child class method 