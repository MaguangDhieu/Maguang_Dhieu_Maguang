class Transaction:
    def __init__(self, employer, balance):
        self.employer = employer
        self.balance = balance

    def process_tranaction(self,amount):
        pass

    def balanceInformation(self, currency = "Ugx"):
        print(f"Current balance:{currency} {self.balance}")

class deposit(Transaction):
    def process_tranaction(self, amount):
        self.balance += amount
        print(f"{self.employer} deposited  {amount}" )
        print(f" New balance:  {self.balance}")

class withdrawal(Transaction):
    def process_tranaction(self, amount):
        if amount <= self.balance:
             self.balance -= amount
             print(f"{self.employer} withdrew  {amount}" )
             print(f" New balance:  {self.balance}")
        else:
            print("Insufficient funds")

class transfer(Transaction):
    def process_tranaction(self, amount, receiver ="Amount Account"):
        if amount <= self.balance:
           self.balance -= amount
           print(f"{self.employer} transferred {amount} to {receiver}" )
           print(f" Remaining balance:  {self.balance}")
        else:
            print("Insufficient funds for transfer")

Deposit = deposit("Maguang", 15000)  
Deposit.process_tranaction(500)  
Deposit.balanceInformation()   

print()

Withdrawal = withdrawal("Maguang",Deposit.balance)
Withdrawal.process_tranaction(300)
Withdrawal.balanceInformation()

print()


Transfer = transfer("Maguang", Withdrawal.balance)
Transfer.process_tranaction(400, "Keth")
Transfer.balanceInformation()