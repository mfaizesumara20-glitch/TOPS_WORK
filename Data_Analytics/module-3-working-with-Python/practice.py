#1. Print numbers from 1 to 10

# for i in range(1,11):
#     print(i)


# revers = 0
# for i in range(1,11):
#     revers-=1

# print(revers)


# i = 1
# while i >= 1:
#     print(i)
#     i+=1


# i = 1

# while i <= 10:
#     print(i)
#     i += 1



# i = 10

# while i >= 1:
#     print(i)
#     i -= 1




# i = 1
# while i<= 20:
#     if i % 2==0:
#         print(i)
#     i +=1




# name = 'Ravi Shah'
# balance = 15000
# amount = int(input('Enter amount to deposit: '))
# def deposit(balance, amount): 
#     return balance + amount
# balance = deposit(balance, amount)

# print('Balance after deposit: ', balance)




class BankBalance:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount

# account1 = BankBalance('Ravi Shah', 15000)
# account1.deposit(5000)

# account2 = BankBalance('John Doe', 20000)
# account2.deposit(10000)

# print(account1.name,'balance after deposit: ', account1.balance)
# print(account2.name,'balance after deposit: ', account2.balance)


# obj = BankBalance(name, balance)
# amount = int(input('Enter amount to deposit: '))
# obj.deposit(amount)
# print('Balance after deposit: ', obj.balance)


