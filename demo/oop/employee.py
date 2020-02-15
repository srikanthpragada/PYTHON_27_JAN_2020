class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def print_details(self):
        print("Name    : ", self.name)
        print("Salary  : ", self.__salary)

    def change_salary(self, newsalary):
        if newsalary > 0:
            self.__salary = newsalary


e1 = Employee("Jack", 200000)
e1.change_salary(300000)
e1.change_salary(-10000)
e1.print_details()
print(e1.__dict__)
