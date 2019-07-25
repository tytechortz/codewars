class Customer():
    def __init__(self, name, balance=0):
        self.name = name 
        self.balance = balance


    def withdrawl(self, x):
        self.balance - x

c1 = Customer("Bill", 1000)

print(c1.balance)

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)