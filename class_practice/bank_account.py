


class BankAccount:
    def __init__(self, first_name, last_name, account_num, balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.account_num = account_num
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(+amount)
        return amount
       
    def withdrawl(self, amount, limit=500):
        if self.balance - amount > 0 and amount <= limit:
            self.balance -= amount
            self.transactions.append(-amount)
            return amount
        else:
            return 'Your withdrawl amount is ${} which exceeds your limit. You have:' \
                '\n${}. Your withdrawl limit is {}'.format(amount, self.balance, limit)

    # def recent_transactions(self):
    #     if len(self.transactions) < 1:
    #         return None
    #     else:
    #         return self.transactions.pop()

    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_account_num(self):
        return self.account_num
    def get_balance(self):
        return self.balance
    def recent_transactions(self):
        if len(self.transactions) < 1:
            return None
        else:
            return self.transactions.pop()

a = BankAccount('Doug', 'Purcell', 3628902828)
print('first name =', a.get_first_name())
print('last name =', a.get_last_name())
print('account number =', a.get_account_num())
print('account balance =', a.get_balance())
print('deposit =', a.deposit(20))
print('recent transaction is:', a.recent_transactions())
print('account balance =', a.get_balance())
print('withdrawal =', a.withdrawl(50))
print('recent transaction is =', a.recent_transactions())
print('account balance =', a.get_balance())

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)