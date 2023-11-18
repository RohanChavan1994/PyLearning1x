# Single inheritance

class Father:

    bank_balance = 500

    def house(self):
        print("Father's house")


class Son(Father):
    pass


son1 = Son()
print(son1.bank_balance)
son1.house()
