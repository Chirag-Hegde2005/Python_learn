# #getters and setters
class Employee:
    def __init__(self,salary):
        self._salary=salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,value):
        if (value < 0):
            print("Salary cannot be negative")
        else:
            self._salary = value
e=Employee(5000)
print(e.salary)
e.salary=-1000
print(e.salary)
