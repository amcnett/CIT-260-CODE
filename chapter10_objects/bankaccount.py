# The BankAccount class simulates a bank account.

class BankAccount:
    
    # The __init__ method accepts an argument for
    # the account's balance. It is assigned to
    # the __balance attribute.
    def __init__(self, bal):
        self.__balance = bal
        self.__transaction_count = 0

    # The deposit method makes a deposit into the
    # account.
    def deposit(self, amount):
        self.__balance += amount
        self.__transaction_count += 1

    # The withdraw method withdraws an amount
    # from the account.
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.__transaction_count += 1
        else:
            print('Error: Insufficient funds')

    # The get_balance method returns the
    # account balance.

    def get_balance(self):
        return self.__balance
    
    def get_transaction_count(self):
        return self.__transaction_count
    
    def __str__(self):
        return f"Balance: {self.__balance}, Transaction Count: {self.__transaction_count}"
    
def main():
  anAccount = BankAccount(100)
  anAccount2 = BankAccount(1000000)
  anAccount3 = BankAccount(0)

  #print(anAccount.__balance)
  print(anAccount.get_balance())
  print(anAccount2.get_balance())
  print(anAccount3.get_balance())

  anAccount.deposit(100) #200
  anAccount.withdraw(50) #150
  anAccount.deposit(100) #250
  anAccount.withdraw(50) #200
  anAccount.withdraw(300) #200
  print(anAccount.get_balance())

  print(anAccount.get_transaction_count())
  print(anAccount)

if __name__=="__main__":
    main()
