class Employee:
    def __init__(self, name, work, wage):
        self.name = name
        self.work = work
        self.wage = wage

    def describe(self):
        print(f"Name: {self.name}, Work: {self.work}, Wage: {self.wage}")

class Department(Employee):
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"New employee {employee.name} had been added to {self.name} department")

    def remove_employee(self, name):
        for emp in self.employees:
            if emp.name == name:
                self.employees.remove(emp)
                print(f"Employee {name} had been removed from {self.name} department")
            else:
                print(f"Employee {name} doesn't exist!")

    def total_wage(self):
        total = 0
        for emp in self.employees:
            total += emp.wage
        print(f"Total wage: {total} grn")

    def show_employees(self):
        if self.employees == []:
            print(f"No employees in {self.name} department!")
        else:
            for emp in self.employees:
                print(emp.name, emp.work, emp.wage)

emp1 = Employee("Evan", "Teacher", 20000)
emp2 = Employee("Arina", "Designer", 30000)
emp3 = Employee("Oleksandr", "Electrical Engineer", 50000)

dep = Department("Kantora")

dep.add_employee(emp1)
dep.add_employee(emp2)
dep.add_employee(emp3)

dep.show_employees()
dep.total_wage()


dep.remove_employee("Evan")

dep.show_employees()
dep.total_wage()

