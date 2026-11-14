# constructor classes
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")
Employee1 = Employee("John", 30, 50000)
Employee2 = Employee("Alice", 25, 60000)
Employee1.display()
Employee2.display()