# For example we build HR System 


def create_emp(first_name, last_name, salary):
    emp_mail = first_name + "." + last_name + "@gmail.com"
    return {'first_name':first_name, 'last_name':last_name, 'emp_mail':emp_mail, 'salary':salary}
    
def raise_salary(emp, amount):
    emp['salary'] = emp['salary'] + amount
    

emp1 = create_emp("Rahul", "Sharma", 30000)
raise_salary(emp1, 5000)
# print(emp1)

#Here is the functions are disconnected 

emp_first = "Rahul"
emp_last = "Sharma"
emp_mail = "rahul.sharma@gmail.com"
emp_sal = 30000

emp_sec_first = "Mohnish"
emp_sec_last = "Trivedi"
emp_sec_mail = "mohnish.trivedi@gmail.com"
emp_sec_sal = 50000 


#200, 000 employees ?? 

# What is object oriented programming ?? 
# Object oriented programming is a programming paradigm that uses "objects" to solve problems 
# 

#Class isa blueprint for creating objects 


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email =  first.lower() + "." + last.lower() + "@gmail.com"
    def full_name(self):
        return f"{self.first} {self.last}" 

    def apply_raise(self, amount):
        self.pay = self.pay + amount
        return self.pay

emp1 = Employee("Rahul", "Sharma", 30000)
emp2 = Employee("Mohnish", "Trivedi", 50000)

# emp1.first = "Rahul"
# emp1.last = "Sharma"
# emp1.mail = "rahul.sharma@gmail.com"
# emp1.salary = 30000

# emp2.first = "Mohnish" 
# emp2.last = "Trivedi"
# emp2.mail = "mohnish.trivedi@gmail.com"
# emp2.salary = 50000

# print(emp1.first)
# print(emp2.email)

# print(emp1.__dict__)

print(emp1.full_name())

print(emp1.apply_raise(5000))

  