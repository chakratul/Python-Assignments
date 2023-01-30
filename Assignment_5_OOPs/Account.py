class Account:
    def __init__(self,title = None,Balance = 0):
        self.title = title
        self.Balance = Balance

    def withdrawal(self,amount):
        self.amount = amount
        withBalance = self.Balance - self.amount
        return withBalance

    def deposit(self,amount):
        self.amount = amount
        depBalance = self.amount + self.Balance
        return (f"Your Current Balance is {depBalance}.")

    def getBalance(self):
        return self.Balance
    
class SavingsAccount(Account):
    def __init__(self,title = None,Balance = 0,interestRate = 0):
        super().__init__(title,Balance)
        self.interestRate = interestRate

    def interestAmount(self,amount):
        self.amount = amount
        intAmount = (self.interestRate *self.Balance)/100
        print(f"Your interest Amount is {intAmount}")



obj1 = Account(Balance = 2000)
obj1.getBalance()
print(obj1.deposit(500))
#obj = SavingsAccount("Ashish",2000,5)
#obj.interestAmount(5)
