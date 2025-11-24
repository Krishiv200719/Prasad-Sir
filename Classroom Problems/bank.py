class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

account = BankAccount("Krishiv", 1000)

account.check_balance()
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)
account.check_balance()
