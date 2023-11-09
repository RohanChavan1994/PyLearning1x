class BankAccount:

    __private_var = 100

    def __init__(self):
        self.balance = 0  # Instance variable -> You can access it via object

    def deposit(self, amount):  # Public method
        self.balance += amount

    def _withdraw(self, amount):  # Protected method
        self.balance -= amount

    def __show_balance(self):  # Private method
        print("Your balance:", self.balance)

    def is_user_verified(self, is_verified):
        if is_verified:
            self.__show_balance()
        else:
            print("User is not verified")

    def bank_manager_withdraw(self, amount):
        self._withdraw(amount)


acc1 = BankAccount()
acc1.deposit(1000)
acc1._withdraw(500)
acc1.bank_manager_withdraw(250)
acc1.is_user_verified(True)

acc1._BankAccount__show_balance()
print(acc1._BankAccount__private_var)
