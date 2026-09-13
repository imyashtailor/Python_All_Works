from abc import ABC,abstractmethod

class BankAccountException(Exception):
    pass

class Account:
    balance = 0
    def check_balance(self):
        print(f"Current Balance is {self.balance}")

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

class Saving(Account):
    def deposit(self, amount):
        self.balance+=amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise BankAccountException("Insufficient Amount")
        else:
            self.balance-=amount

print("Started")
try:
    s1 = Saving()
    s1.check_balance()
    s1.deposit(5000)
    s1.check_balance()
    s1.withdraw(6000)
    s1.check_balance()
except BankAccountException as e:
    print(e)
print("Ended")

