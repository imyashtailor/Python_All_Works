from abc import ABC,abstractmethod

class Account:
    balance = 0
    def check_balance(self):
        print(f"Current Balance is , {self.balance}")
    
    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

class Savings(Account):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

class Loan(Account):
    def deposit(self, amount):
        if amount>self.balance:
            k = amount-self.balance
            print(f"Loan Cleared, you have left {k}")
            self.balance = 0
        else:
            self.balance-=amount 

    def withdraw(self, amount):
        self.balance += amount

# s = Savings()
# s.check_balance()
# s.deposit(5000)
# s.check_balance()

l = Loan()
l.check_balance()
l.withdraw(5000)
l.check_balance()
l.deposit(3000)
l.check_balance()



