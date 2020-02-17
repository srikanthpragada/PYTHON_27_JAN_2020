class Account:
    def __init__(self,acno,customer,balance=0):
        self.__acno = acno
        self.__customer = customer
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def print(self):
        print("Acno     : ",self.__acno)
        print("Customer : ", self.__customer)
        print("Balance  : ",self.__balance)


a1 = Account(1,"Abc")
a1.deposit(10000)
a1.withdraw(5000)
a2 = Account(2,"Pqr",40000)

a1.print()
