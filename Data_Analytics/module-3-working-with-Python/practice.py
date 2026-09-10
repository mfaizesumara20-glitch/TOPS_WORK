3#1. Print numbers from 1 to 10

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


# name = []
# balance = []
# class BankBalance:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance = self.balance + amount

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





# list1 = [1, 2, 3, 4, 5]
# print(list1.append(6))

# print(list1)



# class Customer:

#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
#         self.purchase_history = []

#     def add_purchase(self, amount):
#         self.purchase_history.append(amount)

#     def total_spent(self):
#         return sum(self.purchase_history)

#     def summary(self):
#         print(self.name, '(', self.city,'): Rs', self.total_spent(), 'spent in',len(self.purchase_history), 'orders')


# # Create first customer
# c1 = Customer('Ravi Shah', 28, 'Ahmedabad')

# # Add purchases
# c1.add_purchase(1340)
# c1.add_purchase(520)
# c1.add_purchase(2100)

# # Print summary
# c1.summary()


# # Create second customer
# c2 = Customer('Priya Patel', 34, 'Surat')

# # Add purchase for second customer
# c2.add_purchase(890)

# # Check first customer's total
# print(c1.total_spent())


# class student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
#     def display(self):
#         print('Name:', self.name)
#         print('Age:', self.age)
#         print('Marks:', self.marks)

# std1 = student('Ravi Shah', 20, 85)
# std2 = student('Alan Patel', 22, 90)

# std1.display()
# std2.display()




# class banking:
#     def __init__(self, ac_holder,ac_no, balance):
#         self.ac_holder = ac_holder
#         self.acc_no = ac_no
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance = self.balance + amount
#         return self.balance
#     def withdraw(self,amount):
#         if amount > self.balance:
#             print('Insufficient balance')
#         else:
#             self.balance = self.balance - amount
#         return self.balance
#     def display(self):
#         print('Account Holder:', self.ac_holder)
#         print('Balance:', self.balance)

# cust1 = banking('Ravi Shah', 123456, 15000)
# cust1.deposit(5000)
# cust1.withdraw(2000)
# cust1.display()