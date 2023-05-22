from modules.bank_account import *

# l = []

# l.append(1)

# print(l)

# str = "Hello, Jen"

# print(str.lower())

account = {
    "holder_name": "John",
    "balance": 500,
    "type": "Business",
}

# print(get_account_name(account))

johns_account = BankAccount("John", 500, "Business")
randolph_account = BankAccount("Randolph", 0, "Personal")
pauls_account = BankAccount("Paul", 1000, "Personal")

print(johns_account.balance)
print(randolph_account.type)


# randolph_account.balance = 10
randolph_account.pay_in(100)
print(randolph_account.balance)

johns_account.pay_in(20)
print(johns_account.balance)

pauls_account.pay_monthly_fee()
print(pauls_account.balance)

johns_account.pay_monthly_fee()
print(johns_account.balance)