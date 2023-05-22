# def get_account_name(account):
#     return account["holder_name"]


class BankAccount:
    def __init__(self, holder_name, balance, account_type):
        self.holder_name = holder_name
        self.balance = balance
        self.type = account_type
        self.rates = {
            "Personal": 10,
            "Business": 50,
        }

    def pay_in(self, amount):
        self.balance += amount

    # method: pay_monthly_fee(). to take £50 from an account

    def pay_monthly_fee(self):
            self.balance -= self.rates[self.type]
     

    
