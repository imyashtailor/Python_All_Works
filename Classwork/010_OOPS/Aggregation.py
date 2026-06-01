#Aggregation :- Weak Association
#aano object bahar create karvo
#Has - A relationship :- one object into another 

class salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
    
    def annual_salary(self):
        return (self.pay*12)+self.bonus

class Employee:
    def __init__(self,name,age,s):
        self.name = name
        self.age = age
        self.salary = s
    
    def total_salary(self):
        return self.salary.annual_salary()

s = salary(5000,2000)
e = Employee("Yash",25,s)
print(e.total_salary())