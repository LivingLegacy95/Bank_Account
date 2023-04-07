class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance == 0:
            print("Insuffcient Funds: Charging a 5$ fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self


my_account = BankAccount(.04, 2000)
my_account.deposit(100)
my_account.display_account_info()
my_account.yield_interest()
my_account.display_account_info()
# my_account.withdraw(200)

my_account1 = BankAccount(.02, 500)
my_account1.deposit(200).deposit(50).deposit(100).withdraw(
    200).yield_interest().display_account_info()
print(my_account1.balance)
my_account2 = BankAccount(.04, 5500)
my_account2.deposit(10000).deposit(5000).withdrawal(7000).withdrawal(200).withdrawal(500).withdrawal(1000).yield_interest().display_account_info()
