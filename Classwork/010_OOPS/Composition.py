#Composition :- strong Association and aama aapde class ni under j object banavo pade
#Has - A relationship :- one object into another 

class salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
    
    def annual_salary(self):
        return (self.pay*12)+self.bonus

class Employee:
    def __init__(self,name,age,pay,bonus):
        self.name = name
        self.age = age
        #inside the creating an object in composotion
        self.salary = salary(pay,bonus)
    
    def total_salary(self):
        return self.salary.annual_salary()

e = Employee("Yash",25,5000,2000)
print(e.total_salary())