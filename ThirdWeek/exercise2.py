class MobileMoney:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    @property
    def balance(self):
        return self.__balance


if __name__ == "__main__":
    wallet = MobileMoney()
    wallet.deposit(100)
    try:
        wallet.withdraw(30)
    except ValueError as e:
        print("Error:", e)
    print(wallet.balance)
        